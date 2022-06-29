package com.uai.app.logic.parsers;

import com.uai.app.dominio.Medicamento;
import com.uai.app.dominio.UF;

import org.jsoup.Connection;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;

import java.io.IOException;
import java.util.HashSet;

public abstract class UAIAbstractParser {

    protected String linkToParse;
    protected Document doc;
    protected UF uf;

    public UAIAbstractParser(String linkToParse, UF uf) {
        this.linkToParse = linkToParse;
        this.uf = uf;
    }

    abstract String parsePage(int page);

    public HashSet<Medicamento> getMedicamentos(String principio_activo, int page) throws IOException{
        //realizo la conexion
        Connection.Response response= Jsoup.connect(linkToParse+principio_activo+parsePage(page))
                .ignoreContentType(true)
                .userAgent("Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0")
                .referrer("http://www.google.com")
                .timeout(12000)
                .followRedirects(true)
                .execute();
        doc = response.parse();
        return parseMedicamentos(principio_activo, page);
    }

    public abstract HashSet<Medicamento> parseMedicamentos(String principio_activo, int page) throws IOException;

    protected float getPrecioUF(int precio_pesosChilenos){
        return precio_pesosChilenos/uf.getUf();
    }
}