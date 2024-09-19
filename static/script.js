function crearMatrices() {
    const size = document.getElementById("size").value;
    generarMatriz('matriz1', size);
    generarMatriz('matriz2', size);
    generarMatriz('matriz3', size);
}

function descargarSTL() {
    fetch('static/output.stl')
        .then(response => response.blob())
        .then(blob => {
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'output.stl';
            document.body.appendChild(a);
            a.click();
            a.remove();
            URL.revokeObjectURL(url);
        })
        .catch(error => console.error('Error al descargar el STL:', error));
}

function generarMatriz(matrizId, size) {
    const matrizDiv = document.getElementById(matrizId);
    matrizDiv.innerHTML = '';  
    
    for (let i = 0; i < size; i++) {
        const fila = document.createElement('div');
        
        for (let j = 0; j < size; j++) {
            const input = document.createElement('input');
            input.type = 'checkbox';
            input.checked = true;
            input.name = `${matrizId}[${i}][${j}]`;
            fila.appendChild(input);
        }
        matrizDiv.appendChild(fila);
    }
}

function enviarDatos() {
    const size = document.getElementById("size").value;
    const matriz1 = obtenerMatriz('matriz1', size);
    const matriz2 = obtenerMatriz('matriz2', size);
    const matriz3 = obtenerMatriz('matriz3', size);

    fetch('/procesar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            size: size,
            matriz1: matriz1,
            matriz2: matriz2,
            matriz3: matriz3
        })
    })
    .then(response => response.json())
    .then(data => {
        cargarSTL();
    })
    .catch(error => console.error('Error:', error));
}

function obtenerMatriz(matrizId, size) {
    const matriz = [];
    for (let i = 0; i < size; i++) {
        const fila = [];
        for (let j = 0; j < size; j++) {
            const checkbox = document.querySelector(`input[name="${matrizId}[${i}][${j}]"]`);
            fila.push(checkbox.checked ? true : false);
        }
        matriz.push(fila);
    }
    return matriz;
}
function cargarSTL() {
    const viewer = document.getElementById('viewer');
    viewer.innerHTML = '';  

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, viewer.clientWidth / viewer.clientHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(viewer.clientWidth, viewer.clientHeight);
    viewer.appendChild(renderer.domElement);
    const light = new THREE.DirectionalLight(0xffffff, 1);
    light.position.set(1, 1, 1).normalize();
    scene.add(light);

    const loader = new THREE.STLLoader();
    loader.load('/static/output.stl', function (geometry) {
        const material = new THREE.MeshNormalMaterial();
        const mesh = new THREE.Mesh(geometry, material);
        scene.add(mesh);

        camera.position.z = 5;

        const controls = new THREE.OrbitControls(camera, renderer.domElement);
        controls.enableZoom = true;

        animate();
        
        function animate() {
            requestAnimationFrame(animate);
            renderer.render(scene, camera);
        }
    });
}
