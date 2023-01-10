<!DOCTYPE html>
<html>
<title>
    Ballot
</title>

<body>
    <h2>This is the ballot!</h2>

    <h7>What is your favorite animal?</h7>
    <p>The dog (Canis familiaris or Canis lupus familiaris) is a domesticated descendant of the wolf.</p>
    <p>The cat (Felis catus) is a domestic species of small carnivorous mammal.</p>
    <p>Tardigrades (/ˈtɑːrdɪˌɡreɪdz/), known colloquially as water bears or moss piglets,</p>

    <form action="Submit.php">
    <label for="animals">Choose any option:</label>
    <select name="animals" id="animals" multiple>
        <option value="dog">Dog</option>
        <option value="cat">Cat</option>
        <option value="tardigrade">Tardigrade</option>
    </select>
    <br><br>
    <input type="submit" value="Submit">
    </form>

    <p>Hold down the Ctrl (windows) or Command (Mac) button to select multiple options.</p>
</body>