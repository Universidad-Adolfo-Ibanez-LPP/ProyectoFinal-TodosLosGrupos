package com.uai.app.logic.parsers;

import java.io.IOException;
import java.util.HashSet;

import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import com.uai.app.dominio.Medicamento;
import com.uai.app.dominio.UF;

public class AhumadaParser extends UAIAbstractParser {

    public AhumadaParser(UF uf) {
        super("https://www.farmaciasahumada.cl/catalogsearch/result/index/?q=", uf);
    }

    
    @Override
    String parsePage(int page) {
        return "&p=" + Integer.toString(page); 
    }

    @Override
    public HashSet<Medicamento> parseMedicamentos(String principio_activo, int page) throws IOException {
        HashSet<Medicamento> medicamentos = new HashSet<Medicamento>();

        Elements currentPage = doc.getElementsByClass("current");
        Elements pageElements = currentPage.get(0).getElementsByClass("page");
        String pageNumberString = pageElements.get(0).getElementsByIndexEquals(1).text();
        int currentPageInt = Integer.parseInt(pageNumberString);
        if(page > currentPageInt){
            return medicamentos;
        }


        Elements container = doc.getElementsByClass("product-items");
        Elements medicamentosElements = container.get(0).getElementsByClass("product-item");

        for (Element card : medicamentosElements) {
            //Creo medicamento
            Medicamento medicamento = new Medicamento();
            //Cargo la farmacia
            medicamento.setFarmacia("ahumada");
            //Cargo el principio activo
            medicamento.setPrincipio_activo(principio_activo);
            //Descripcion del medicamento
            Elements descripcionElements = card.getElementsByClass("product-item-link");
            String descripcionString = descripcionElements.get(0).text();
            medicamento.setDescripcion(descripcionString);
            //Precio en pesos chilenos
            Elements priceElements = card.getElementsByClass("price");
            String priceString = priceElements.get(0).text();
            priceString = priceString.replace("$", "");
            priceString = priceString.replace(".", "");
            priceString = priceString.replace(",", ".");
            medicamento.setPrecio_pesosChilenos(Integer.parseInt(priceString));
            //Pesos en UF
            medicamento.setPrecioUF(getPrecioUF(medicamento.getPrecio_pesosChilenos()));
            
            //cargo el medicamento en el set
            medicamentos.add(medicamento);
        }
        return medicamentos;
    }

    
}
