package com.uai.app.logic;

import com.uai.app.dominio.Medicamento;
import com.uai.app.dominio.enums.Tittles;
import org.apache.commons.text.CaseUtils;
import org.apache.commons.text.similarity.LevenshteinDistance;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.*;

/*
 * Esta clase me sirve para filtrar la data que tenemos en DataManager
 * Acorde a ciertos criterios o formas de busqueda
 * Para valores que no sean numericos utiliza distancia de Levenshtein
 */
public class SearchManager {

    //nos dice la precision en la busqueda el numero
    // cuanto mas cercano a 0 es mas exacta la busqueda
    // cuanto mas lejano menos exacta
    // Chila difiere en 1 de Chile por ejemplo
    public static final int FILTER_MAX_DISTANCE = 4;

    //lo que me servira para medir las distancias entre dos strings
    private static LevenshteinDistance lv = new LevenshteinDistance();

    private static SearchManager instance;

    //todos los singletons
    // tienen constructores privados
    private SearchManager(){

    }

    // como todo singleton este metodo
    //  para acceder la unica instancia
    public static SearchManager getInstance(){
        if (instance == null){
            instance = new SearchManager();
        }
        return instance;
    }

    /*
     * Esto usa la distancia de Levenshtein
     * para buscar, para llamarlo tenemos que
     * pasarle un valor de una enumeracion que se corresponde
     * al campo donde vamos a buscar, supongamos country,
     * queremos que nos devuelvan todas las personas
     * que viven en Chile, por lo que lo llamamos
     *
     * findPersonByAttribute(Tittles.COUNTRY, "Chile")
     *
     * si quisieramos todas las personas de nombre David
     * Entonces deberiamos llamarlo de la siguiente forma
     *
     * findPersonByAttribute(Tittles.NAME, "David")
     */

    /*
     * Esto usa la distancia de Levenshtein
     * para buscar, para llamarlo tenemos que
     * pasarle un valor de una enumeracion que se corresponde
     * al campo donde vamos a buscar, supongamos country,
     * queremos que nos devuelvan todas las personas
     * que viven en Chile, por lo que lo llamamos
     *
     * findPersonByAttribute(Tittles.COUNTRY, "Chile")
     *
     * si quisieramos todas las personas de nombre David
     * Entonces deberiamos llamarlo de la siguiente forma
     *
     * findPersonByAttribute(Tittles.NAME, "David")
     *
     * SI queremos especificar nosotros la precision
     *  y que no sea siempre 4 llamamos al metodo de abajo
     */
    public HashSet<Medicamento> findPersonByAttribute(Tittles title, String theSearch){
        return findPersonByAttribute(title, theSearch, FILTER_MAX_DISTANCE);
    }

    //mismo metodo que el de arriba solo que pedimos la precision
    public HashSet<Medicamento> findPersonByAttribute(Tittles title, String theSearch, int precision){
        //ahora instancio un mapa con esas claves
        HashSet<Medicamento> data = DataManager.getInstance().getData();;
        HashSet<Medicamento> ciudadanos = new HashSet<Medicamento>();
        for (Medicamento p : data){
            //Uso lo mismo que en el data manager
            Class<?> classObj = p.getClass();
            Method printMessage = null;
            try {
                String camelCase = CaseUtils.toCamelCase(title.getVal(), true);
                printMessage = classObj.getDeclaredMethod("get"+camelCase);
                String filterName = String.valueOf(printMessage.invoke(p));

                // si es un numero entonces no uso distancia de leventeihns
                if (printMessage.getReturnType().isPrimitive() ||
                        printMessage.getReturnType().isAssignableFrom(Integer.class)){
                    if (theSearch.trim().equalsIgnoreCase(filterName)){
                        ciudadanos.add(p);
                    }
                } else {
                    //Con una distancia de 3 estamos bien cubiertos
                    if (lv.apply(theSearch, filterName) < precision){
                        ciudadanos.add(p);
                    }
                }


            } catch (IllegalAccessException e) {
                e.printStackTrace();
            } catch (InvocationTargetException e) {
                e.printStackTrace();
            } catch (NoSuchMethodException e) {
                e.printStackTrace();
            }

        }
        return ciudadanos;
    }



    /*
     * Este metodo devuelve conjuntos de personas
     *  agrupados por grupos acorde a una columna//atributo
     * de la persona. Si lo llamamos asi
     *
     * getPeopleByColum(Tittles.COUNTRY)
     *
     * va a devolver un mapa donde cada clave es el pais y asociado
     * como valor tendran las personas que viven en ese pais
     * esto es util cuando me piden por ejemplo todos los libros de una seccion etc
     */
    public Map<String, Set<Medicamento>> getPeopleByColum(Tittles columName){
        //ahora instancio un mapa con esas claves
        Map<String, Set<Medicamento>> resultados = new HashMap<>();
        HashSet<Medicamento> data = DataManager.getInstance().getData();;
        for (Medicamento p : data){
            //primero debo saber que atributo
            // es para saber a que get llamare
            // esto se denomina llamar
            // a metodos por reflexion
            Class<?> classObj = p.getClass();
            Method printMessage = null;
            try {
                String camelCase = CaseUtils.toCamelCase(columName.getVal(), true);
                printMessage = classObj.getDeclaredMethod("get"+camelCase);
                String filterName = String.valueOf(printMessage.invoke(p));
                Set<Medicamento> ciudadanos = resultados.get(filterName);
                ciudadanos.add(p);
                resultados.put(filterName, ciudadanos);

            } catch (IllegalAccessException e) {
                e.printStackTrace();
            } catch (InvocationTargetException e) {
                e.printStackTrace();
            } catch (NoSuchMethodException e) {
                e.printStackTrace();
            }

        }
        return resultados;
    }
}
