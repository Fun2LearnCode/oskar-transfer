#pragma strict

public var frontWheel : GameObject ;
public var rearWheel :GameObject ;

function SetSpeed (speed : float) {
	frontWheel.GetComponent.<WheelJoint2D>().motor.motorSpeed = speed;
	rearWheel.GetComponent.<WheelJoint2D>().motor.motorSpeed = speed;
	}

function Update () 
{
}