#pragma strict

function Start () {
	Invoke("EndCrash", .5);
}

function EndCrash () {
	Destroy(gameObject);
}
