package com.uai.app.files;

import com.opencsv.CSVWriter;
import com.uai.app.logic.DataManager;
import com.uai.app.dominio.Medicamento;

import java.io.*;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

import static com.opencsv.ICSVWriter.*;

public class FileManager {

    private File inFile;
    private File outFile;

    private String[] titles = {"principio activo","farmacia","descripcion","precio pesos chilenos", "precio UF"};
    /*
    Reviso si existe el archivo que me van a hacer ocupar
    y sino tiro una excepcion para arriba
     */
    public FileManager(String fileName, String outFilename) throws FileNotFoundException {
        this.inFile = new File(fileName);
        if (!inFile.exists()){
            throw new FileNotFoundException();
        }
        this.outFile = new File(outFilename);
    }

    public List<String> getData() {
        List<String> principios = new ArrayList<>();
        String line;

        try {
    
            BufferedReader bufferreader = new BufferedReader(new FileReader(inFile));
            while ((line = bufferreader.readLine()) != null) {
                principios.add(line.trim());
            }
    
        } catch (FileNotFoundException ex) {
            ex.printStackTrace();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        return principios;
    }

    public void saveData(){
        try {
            FileWriter t = new FileWriter(outFile.getName());
            CSVWriter writer = new CSVWriter(t, ',', DEFAULT_QUOTE_CHARACTER, DEFAULT_ESCAPE_CHARACTER, DEFAULT_LINE_END);
            // Aca convierto al csv que necesito
            writer.writeNext(titles, false);
            HashSet<Medicamento> data = DataManager.getInstance().getData();

            for(Medicamento p : data){
                //significa que lo quiero mantener
                writer.writeNext(p.getDataToCsv(),false);
            }
            writer.close();

        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
