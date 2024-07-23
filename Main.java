public class Main {
    public static void main(String[] args) {
        // Create and manipulate your linked list here
        // Example:
        LinkedList<Person> list = new LinkedList<>();
        // Add persons to the list and call list.reverse()
    }

    public void reverse() {
        if (firstPerson == null || size() <= 1) {
            return; // List is empty or has only one element
        }

        Person<T> current = firstPerson;
        Person<T> previous = null;
        Person<T> next = null;

        while (current != null) {
            next = current.getNextPerson();
            current.setNextPerson(previous);
            previous = current;
            current = next;
        }

        firstPerson = previous; // Update the head of the list
    }
}
