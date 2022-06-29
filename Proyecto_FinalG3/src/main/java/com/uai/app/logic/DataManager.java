package com.uai.app.logic;

import com.uai.app.dominio.Medicamento;
import com.uai.app.exceptions.DataNotLoadedException;
import java.util.*;

/*
*
* Dado que solo necesitare una instancia de esta clase
* la convierto en SIngleton https://refactoring.guru/design-patterns/singleton
*
 */
public class DataManager {

    private HashSet<Medicamento> data = new HashSet<>();

    private static DataManager instance;

    //todos los singletons
    // tienen constructores privados
    private  DataManager(){
        
    }

    public static DataManager getInstance(){
        if (instance == null){
            instance = new DataManager();
            SearchManager.getInstance();
        }
        return instance;
    }

    public HashSet<Medicamento> getData() {
        return data;
    }

    public void setData(HashSet<Medicamento> data) {
        this.data = data;
    }

    public String getDataAsString() throws DataNotLoadedException {
        //Creo un string para ir sumando ahi la data
        StringBuilder sb = new StringBuilder(data.size()*50);
        for (Medicamento p : data){
               sb.append(p);
               sb.append("\n");
        }
        return sb.toString();
    }

    public void agregarMedicamento(Medicamento p){
        this.data.add(p);
    }

    public void removerMedicamento(Medicamento p){
        this.data.remove(p);
    }

    public void removerMedicamentos(Collection<Medicamento> personas){
        this.data.removeAll(personas);
    }
}
