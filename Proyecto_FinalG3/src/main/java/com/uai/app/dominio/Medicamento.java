package com.uai.app.dominio;

import java.util.Objects;

import org.jsoup.select.Elements;

import com.opencsv.bean.CsvBindByName;

public class Medicamento {
    @CsvBindByName(column = "principio activo")
    private String principio_activo;
    @CsvBindByName(column = "farmacia")
    private String farmacia;
    @CsvBindByName(column = "descripcion")
    private String descripcion;
    @CsvBindByName(column = "precio pesos chilenos")
    private int precio_pesosChilenos;
    @CsvBindByName(column = "precio UF")
    private float precioUF;


    public Medicamento() {
    }

    public Medicamento(String principio_activo, String farmacia, String descripcion, int precio_pesosChilenos, float precioUF) {
        this.principio_activo = principio_activo;
        this.farmacia = farmacia;
        this.descripcion = descripcion;
        this.precio_pesosChilenos = precio_pesosChilenos;
        this.precioUF = precioUF;
    }

    public String getPrincipio_activo() {
        return this.principio_activo;
    }

    public void setPrincipio_activo(String principio_activo) {
        this.principio_activo = principio_activo;
    }

    public String getFarmacia() {
        return this.farmacia;
    }

    public void setFarmacia(String farmacia) {
        this.farmacia = farmacia;
    }

    public String getDescripcion() {
        return this.descripcion;
    }

    public void setDescripcion(String descripcionElements) {
        this.descripcion = descripcionElements;
    }

    public int getPrecio_pesosChilenos() {
        return this.precio_pesosChilenos;
    }

    public void setPrecio_pesosChilenos(int precio_pesosChilenos) {
        this.precio_pesosChilenos = precio_pesosChilenos;
    }

    public float getPrecioUF() {
        return this.precioUF;
    }

    public void setPrecioUF(float precioUF) {
        this.precioUF = precioUF;
    }

    public Medicamento principio_activo(String principio_activo) {
        setPrincipio_activo(principio_activo);
        return this;
    }

    public Medicamento farmacia(String farmacia) {
        setFarmacia(farmacia);
        return this;
    }

    public Medicamento descripcion(String descripcion) {
        setDescripcion(descripcion);
        return this;
    }

    public Medicamento precio_pesosChilenos(int precio_pesosChilenos) {
        setPrecio_pesosChilenos(precio_pesosChilenos);
        return this;
    }

    public Medicamento precioUF(float precioUF) {
        setPrecioUF(precioUF);
        return this;
    }

    @Override
    public boolean equals(Object o) {
        if (o == this)
            return true;
        if (!(o instanceof Medicamento)) {
            return false;
        }
        Medicamento medicamento = (Medicamento) o;
        return Objects.equals(principio_activo, medicamento.principio_activo) && Objects.equals(farmacia, medicamento.farmacia) && Objects.equals(descripcion, medicamento.descripcion) && precio_pesosChilenos == medicamento.precio_pesosChilenos && precioUF == medicamento.precioUF;
    }

    @Override
    public int hashCode() {
        return Objects.hash(principio_activo, farmacia, descripcion, precio_pesosChilenos, precioUF);
    }

    @Override
    public String toString() {
        return "{" +
            " principio_activo='" + getPrincipio_activo() + "'" +
            ", farmacia='" + getFarmacia() + "'" +
            ", descripcion='" + getDescripcion() + "'" +
            ", precio_pesosChilenos='" + getPrecio_pesosChilenos() + "'" +
            ", precioUF='" + getPrecioUF() + "'" +
            "}";
    }


    public String[] getDataToCsv(){
        // el string.valueOf me convierte el int a string
        return new String[]{ getPrincipio_activo().trim(), getFarmacia().trim(), getDescripcion().trim(), String.valueOf(getPrecio_pesosChilenos()), String.valueOf(getPrecioUF())};
    }
   
}
