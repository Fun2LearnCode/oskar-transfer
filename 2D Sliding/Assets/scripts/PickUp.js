#pragma strict
public var pickupEffect : GameObject;

function OnTriggerEnter2D (other : Collider2D)
	{
	if (pickupEffect)
	Instantiate(pickupEffect, transform.position, transform.rotation);

	Destroy(gameObject);
	}