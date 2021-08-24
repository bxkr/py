window.onload = function () {
    Object.entries(outputs).forEach((script) => {
        const codeDiv = document.createElement('div');
        codeDiv.className = 'code';
        const filenameDiv = document.createElement('div');
        filenameDiv.className = 'filename';
        filenameDiv.innerHTML = `Файл: ${script[0]}`;
        const preElement = document.createElement('pre');
        preElement.innerHTML = script[1];
        codeDiv.appendChild(filenameDiv);
        codeDiv.appendChild(preElement);
        document.getElementById('outputs').appendChild(codeDiv);
    });
}