package com.uai.app.dominio.enums;

public enum Tittles {

    principio_activo("principio activo"),FARMACIA("farmacia"),DESCRIPCION("descripcion"),PRECIO_PESOSCHILENOS("precio pesos chilenos"),PRECIOUF("precio UF");

    private String val;

    public String getVal() {
        return val;
    }

    Tittles(String val) {
        this.val = val;
    }

}
