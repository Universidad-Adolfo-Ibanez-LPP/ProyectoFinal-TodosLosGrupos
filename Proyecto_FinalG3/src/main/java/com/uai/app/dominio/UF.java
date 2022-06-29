package com.uai.app.dominio;

import java.util.Objects;

import com.opencsv.bean.CsvBindByName;

public class UF {
    @CsvBindByName(column = "uf")
    private float uf;
    @CsvBindByName(column = "fecha")
    private String fecha;


    public UF() {
    }

    public UF(float uf, String fecha) {
        this.uf = uf;
        this.fecha = fecha;
    }

    public float getUf() {
        return this.uf;
    }

    public void setUf(float uf) {
        this.uf = uf;
    }

    public String getFecha() {
        return this.fecha;
    }

    public void setFecha(String fecha) {
        this.fecha = fecha;
    }

    public UF uf(float uf) {
        setUf(uf);
        return this;
    }

    public UF fecha(String fecha) {
        setFecha(fecha);
        return this;
    }

    @Override
    public boolean equals(Object o) {
        if (o == this)
            return true;
        if (!(o instanceof UF)) {
            return false;
        }
        UF uF = (UF) o;
        return uf == uF.uf && Objects.equals(fecha, uF.fecha);
    }

    @Override
    public int hashCode() {
        return Objects.hash(uf, fecha);
    }

    @Override
    public String toString() {
        return "{" +
            " uf='" + getUf() + "'" +
            ", fecha='" + getFecha() + "'" +
            "}";
    }


    public String[] getDataToCsv(){
        // el string.valueOf me convierte el int a string
        return new String[]{ getFecha().trim(), String.valueOf(getUf())};
    }
    
}
