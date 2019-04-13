using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class moneys : MonoBehaviour {
	public int points;

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		
	}
	void OnTriggerEnter2D(Collider2D colider){
		if(colider.tag == "player"){
			Debug.Log ("omm nomm "+points);
			Destroy (gameObject);
		}
	}

}
