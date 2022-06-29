package com.uai.app.logic.parsers;

import java.io.IOException;
import java.text.SimpleDateFormat;

import org.jsoup.Connection;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import com.uai.app.dominio.UF;

public class BancoCentralParser {

    protected String linkToParse;
    protected Document doc;
    protected SimpleDateFormat formatter;

    public BancoCentralParser(String linkToParse) {
        this.linkToParse = linkToParse;
        formatter = new SimpleDateFormat("dd/MM/yyyy");
    }

    public UF getUF() throws IOException{
        //realizo la conexion
        Connection.Response response= Jsoup.connect(linkToParse)
                .ignoreContentType(true)
                .userAgent("Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0")
                .referrer("http://www.google.com")
                .timeout(12000)
                .followRedirects(true)
                .execute();
        doc = response.parse();
        return parseUF();
    }

    private UF parseUF() {
        Elements fechaElements = doc.getElementsByClass("fin-indicators-col1");
        if(fechaElements.size() > 0){
            Element fechaElement = fechaElements.get(0);
            Elements fechas = fechaElement.getElementsByClass("fs-1");
            String fechaString = fechas.get(0).text();
            Elements ufElements = doc.getElementsByAttributeValue("title", "UF: Unidad de Fomento");
        
            for (Element uf : ufElements) {
                Elements ufsValues = uf.getElementsByClass("fs-2");
                if(ufsValues.size() > 0){
                    Element ufElement = ufsValues.get(0);
                    String ufString = ufElement.text();
                    ufString = ufString.replace("$", "");
                    ufString = ufString.replace(".", "");
                    ufString = ufString.replace(",", ".");
                    float ufValue = Float.parseFloat(ufString);
                    return new UF(ufValue, fechaString);

                }
            }
        }
    
        return null;
    }

    
}
