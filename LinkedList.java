class LinkedList<T> {
  private Person<T> firstPerson;

  // Other methods to manage the list

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

  public int size() {
      // Implement size calculation
      return 0;
  }
}
