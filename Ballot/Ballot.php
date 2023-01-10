<!DOCTYPE html>
<html>
<title>
    Ballot
</title>

<body>
    <h1>This is the ballot! Multiple Votes Allowed!</h1>

    <form action="Submit.php" method="post">
        <div>
            <h3>What is your favorite animal? (Multi vote available)</h3>
            <p>The dog (Canis familiaris or Canis lupus familiaris) is a domesticated descendant of the wolf.</p>
            <p>The cat (Felis catus) is a domestic species of small carnivorous mammal.</p>
            <p>Tardigrades (/ˈtɑːrdɪˌɡreɪdz/), known colloquially as water bears or moss piglets.</p>
        </div>
        <input type="checkbox" id="dog" name="vote_1[]" value="dog">
        <label for="dog">Support Dog</label><br>
        <input type="checkbox" id="cat" name="vote_1[]" value="cat">
        <label for="cat">Support Cat</label><br>
        <input type="checkbox" id="tardigrade" name="vote_1[]" value="tardigrade">
        <label for="tardigrade">Support Tardigrade</label><br>
        
        
        <div>
            <h3>What is your favorite food? (Multi vote available)</h3>
            <p>Packaged crème caramel is ubiquitous in Japanese convenience stores under the name purin (プリン) (i.e., "pudding"), or custard pudding.</p>
            <p>Mochi (もち, 餅) is a Japanese rice cake made of mochigome (もち米), a short-grain japonica glutinous rice, and sometimes other ingredients such as water, sugar, and cornstarch.</p>
            <p>Paimon is an NPC in Genshin Impact who accompanies the Traveler throughout their adventure in Teyvat as their guide.</p>
            <p>Dango (団子) is a Japanese dumpling made from rice flour mixed with uruchi rice flour and glutinous rice flour.</p>
        </div>
        <input type="checkbox" id="purin" name="vote_2[]" value="purin">
        <label for="pudding_cup">Support Purin</label><br>
        <input type="checkbox" id="mochi" name="vote_2[]" value="mochi">
        <label for="mochi">Support Mochi</label><br>
        <input type="checkbox" id="emergency_food" name="vote_2[]" value="emergency food">
        <label for="emergency_food">Support Paimon</label><br>
        <input type="checkbox" id="dango" name="vote_2[]" value="dango">
        <label for="dango">Support Dango</label><br>
        
        <br><br><input type="submit" value="Submit">
    </form>
    <br>
    <br>


    <form action="Submit.php" method="post">

    </form>
    <br>
    <br>   
</body>