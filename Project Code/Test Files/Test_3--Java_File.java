/*
Name: Film.java
Author: Wesley Lee wtl5736@rit.edu
Date: 03-10-2016
*/


import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;


/**
 * Class representing a film.
 */
public class Film {

    private String name;
    private List<Film> neighbors;
    final private List<String> actors;


    /**
     * Constructor.  Initialized with an empty list of neighbors.
     * and a filled list of known actors. This list is final because the actors of
     * a film should never change
     *
     * @param name string representing the name associated with the node.
     * @param actors ArrayList containing all known actors of the film
     *
     */
    public Film(String name, ArrayList actors) {

        this.name = name;
        this.neighbors = new LinkedList<>();
        this.actors = actors;

    }


    /**
     * Gets the List of actors
     *
     * @return actors
     */

    public List<String> getActors() {

        return actors;

    }


    /**
     * Get the String name associated with this object.
     *
     * @return name.
     */
    public String getName() {

        return name;

    }


    /**
     * Add a neighbor to this Film.  Checks if already present, and does not
     * duplicate in this case.
     *
     * @param f: Film to add as neighbor.
     */
    public void addNeighbor(Film f) {

        if (!neighbors.contains(f)) {

            neighbors.add(f);

        }
    }


    /**
     * Method to return the adjacency list for this node containing all
     * of its neighbors.
     *
     * @return the list of neighbors of the given Movie
     */
    public List<Film> getNeighbors() {

        return new LinkedList<>(neighbors);

    }


    /**
     * Method to generate a string associated with the Film, including the
     * name of the Film followed by the names of its actors.  Overrides
     * Object toString method.
     *
     * @return string associated with the node.
     */
    @Override
    public String toString() {

        String result;
        result = "Name:" + name + "\n\t" + "Actors: " + this.actors.toString();

        return result;
    }


    /**
     * Two films are equal if they have the same name.
     *
     * @param other The other object to check equality with
     * @return true if equal; false otherwise
     */
    @Override
    public boolean equals(Object other) {

        boolean result = false;
        if (other instanceof Film) {

            Film f = (Film) other;
            result = this.name.equals(f.name);

        }

        return result;

    }
}
