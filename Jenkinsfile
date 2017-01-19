echo 'hello world!!';

node{
    stage('Fetch'){
        checkout scm;
    }
    stage('Test') {
        echo 'Testing';
        sh 'python seventh.py';
        assert true;
    }

    stage('Build') { // <2>
        echo 'building';// <3>
    }

    stage('kabutar'){
        echo 'gutur gu!! gutur gu!!'
    }

}
