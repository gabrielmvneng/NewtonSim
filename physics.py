def handle_gravity(bodies, dt, G):
    for i in range(len(bodies)):
        body = bodies[i]
        for j in range(i + 1, len(bodies)):
            next_body = bodies[j]

def wall_collision(width, height, dt, bodies):
    for body in bodies:
        if width - body.position.x < body.radius or body.position.x <= body.radius:
            body.velocity.x = -body.velocity.x
        if height - body.position.y < body.radius or body.position.y <= body.radius:
            body.velocity.y = -body.velocity.y

def move_and_slide(bodies, dt):
    for body in bodies:
        body.position += body.velocity * dt

def physics_update(width, height, dt, bodies, G):
        move_and_slide(bodies, dt)
        wall_collision(width, height, dt, bodies)
