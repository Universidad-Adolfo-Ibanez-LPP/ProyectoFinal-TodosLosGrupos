package com.uai.app.logic;

import com.uai.app.dominio.Medicamento;
import com.uai.app.dominio.UF;
import com.uai.app.logic.parsers.AhumadaParser;
import com.uai.app.logic.parsers.FarmazonParser;
import com.uai.app.logic.parsers.UAIAbstractParser;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

/*
  * Esta clase maneja todos los parsers que posee mi codigo
  * Obtiene una respuesta de cada uno y los devuelve
 */
public class ParserManager {
    
    private List<UAIAbstractParser> parsers;
    
    public ParserManager(UF uf){
        this.parsers = new ArrayList<UAIAbstractParser>();
        parsers.add(new AhumadaParser(uf));
        parsers.add(new FarmazonParser(uf));
    }

    public HashSet<Medicamento> getMedicamentos(String principio) {
        HashSet<Medicamento> medicamentos = new HashSet<Medicamento>();
        for (UAIAbstractParser parser : parsers) {
            int page = 0;
            HashSet<Medicamento> medicamentosParser;
            
            try{
                do {
                    page++;
                    medicamentosParser = parser.getMedicamentos(principio, page);
                    medicamentos.addAll(medicamentosParser);
                } while(medicamentosParser!=null && medicamentosParser.size() > 0);
            } catch (IOException e) {
               System.err.println("Error obteniendo medicamentos");
               e.printStackTrace();
            }
        }
        return medicamentos;
    }
}
