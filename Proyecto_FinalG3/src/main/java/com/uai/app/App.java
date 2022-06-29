package com.uai.app;

import com.uai.app.dominio.Medicamento;
import com.uai.app.dominio.UF;
import com.uai.app.exceptions.CSVNotFoundException;
import com.uai.app.files.FileManager;
import com.uai.app.files.UFFileManager;
import com.uai.app.logic.DataManager;
import com.uai.app.logic.ParserManager;
import com.uai.app.logic.parsers.BancoCentralParser;

import java.io.*;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Optional;
import java.util.OptionalDouble;
import java.util.stream.Collector;
import java.util.stream.Collectors;

/**
 * Hello world!
 *
 */
public class App {

    public static void main( String[] args ) throws IOException {
        System.out.println("COMENZANDO");
        String fileName = args[0];


        try {
            //instancio el file manager
            FileManager f = new FileManager(fileName, "medicamentos.csv");
            UFFileManager ufFileManager = new UFFileManager("parametros.csv");
            BancoCentralParser bancoCentralParser = new BancoCentralParser("https://www.bcentral.cl/inicio");
            UF uf = bancoCentralParser.getUF();
            ufFileManager.saveData(uf);
            
            //Obtener instancia del data manager
            DataManager dataManager = DataManager.getInstance();
            //Obtener los principios del archivo
            List<String> principios = f.getData();
            ParserManager parserManager = new ParserManager(uf);
            //Para cada principio, obtengo todos los medicamentos
            for(String principio: principios){
                System.out.println(principio);
                HashSet<Medicamento> medicamentos = parserManager.getMedicamentos(principio);
                //Agrego los medicamentos al data manager
                for(Medicamento medicamento: medicamentos){
                    dataManager.agregarMedicamento(medicamento);
                }
            }
            f.saveData();

            //Estadísticos hechos con paradigma funcional:
            HashSet<Medicamento> data = dataManager.getData();
            //Minimo por principio
            List<Optional<Medicamento>> minPorPrincipio = data
            .stream()
            .collect(Collectors.groupingBy(Medicamento::getPrincipio_activo))
            .values()
            .stream()
            .map(medicamentos -> medicamentos.stream().min(Comparator.comparing(Medicamento::getPrecio_pesosChilenos)))
            .collect(Collectors.toList());


            //Máximo por principio
            List<Optional<Medicamento>> maxPorPrincipio = data
            .stream()
            .collect(Collectors.groupingBy(Medicamento::getPrincipio_activo))
            .values()
            .stream()
            .map(medicamentos -> medicamentos.stream().max(Comparator.comparing(Medicamento::getPrecio_pesosChilenos)))
            .collect(Collectors.toList());


            //Contar medicamentos por principio
            List<Long> medicamentosPorPrincipio = data
            .stream()
            .collect(Collectors.groupingBy(Medicamento::getPrincipio_activo))
            .values()
            .stream()
            .map(medicamentos -> medicamentos.stream().count())
            .collect(Collectors.toList());

            //Promedio de precio por principio
            List<OptionalDouble> promedioPorPrincipio = data
            .stream()
            .collect(Collectors.groupingBy(Medicamento::getPrincipio_activo))
            .values()
            .stream()
            .map(medicamentos -> medicamentos.stream().mapToDouble(
                medicamento ->  medicamento.getPrecio_pesosChilenos()/medicamentos.size())
            ).map(doubleStream -> doubleStream.reduce(Double::sum))
            .collect(Collectors.toList());


            //Mediana de precio por principio
            List<Integer> medianaPorPrincipio = data
            .stream()
            .collect(Collectors.groupingBy(Medicamento::getPrincipio_activo))
            .values()
            .stream()
            .map(medicamentos -> medicamentos.stream().sorted(Comparator.comparing(Medicamento::getPrecio_pesosChilenos)).collect(Collectors.toList()))
            .map(medicamentos -> {
                if(medicamentos.size() % 2 == 0){
                    return (medicamentos.get(medicamentos.size()/2).getPrecio_pesosChilenos() + medicamentos.get(medicamentos.size()/2 - 1).getPrecio_pesosChilenos()) / 2;
                }
                else{
                    return medicamentos.get((int) Math.floor(medicamentos.size()/2)).getPrecio_pesosChilenos();
                }
            })
            .collect(Collectors.toList());


        } catch (CSVNotFoundException e) {
            System.out.println(e.getMessage());
            e.printStackTrace();
        }

    }
}
