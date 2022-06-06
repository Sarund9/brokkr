package app

import "core:fmt"
// import "core:runtime"

Vec3 :: struct {
    x, y, z : f32,
}

@export
init :: proc() { 
    fmt.println("Test Working!");
    
}
