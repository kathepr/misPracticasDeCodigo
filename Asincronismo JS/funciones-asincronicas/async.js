async function showData() {
    try {
        const json = await getData();
        console.table(json);
    } catch (error) {
        console.error(error);
    }
}

const getData = async () => {
    const response = await fetch("https://jsonplaceholder.typicode.com/posts/4");
    const json = await response.json(); //  lee el cuerpo de la respuesta y lo convierte a JSON (JavaScript Object Notation).
    return json;
};

showData();