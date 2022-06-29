package com.uai.app.files;

import com.opencsv.CSVWriter;
import com.uai.app.dominio.UF;
import com.uai.app.exceptions.CSVNotFoundException;

import java.io.*;

import static com.opencsv.ICSVWriter.*;

public class UFFileManager {

    private File theFile;

    /*
    Reviso si existe el archivo que me van a hacer ocupar
    y sino tiro una excepcion para arriba
     */
    public UFFileManager(String fileName) throws CSVNotFoundException {
        this.theFile = new File(fileName);
    }

    public void saveData(UF uf){
        try {
            FileWriter t = new FileWriter(theFile.getName());
            CSVWriter writer = new CSVWriter(t, ',', DEFAULT_QUOTE_CHARACTER, DEFAULT_ESCAPE_CHARACTER, DEFAULT_LINE_END);
            writer.writeNext(uf.getDataToCsv(),false);
            writer.close();

        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
