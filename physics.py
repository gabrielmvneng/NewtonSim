from pygame.math import Vector2

def calculate_gravity(body1, body2, G):
    direction = body2.position - body1.position
    direction_normalized = direction.normalize()
    distance = direction.length()
    f_g = G * (body1.mass * body2.mass) / distance ** 2
    return direction_normalized * f_g

def collide(body1, body2, normal, distance):
    penetration = body1.radius + body2.radius - distance

    body1.position -= normal * (penetration / 2)
    body2.position += normal * (penetration / 2)

    velocity1 = body1.velocity.dot(normal)
    velocity2 = body2.velocity.dot(normal)

    body1.velocity -= normal * velocity1 * 2
    body2.velocity -= normal * velocity2 * 2

def apply_gravity(body1, body2, dt, force_vec):
    acceleration_1 = force_vec/body1.mass
    acceleration_2 = -force_vec/body2.mass
    body1.velocity += acceleration_1 * dt
    body2.velocity += acceleration_2 * dt

def handle_gravity(bodies, dt, G):
    for i in range(len(bodies)):
        body = bodies[i]
        for j in range(i + 1, len(bodies)):
            next_body = bodies[j]
            force_vec = calculate_gravity(body, next_body, G)
            apply_gravity(body, next_body, dt, force_vec)

def wall_collision(width, height, bodies):
    for body in bodies:
        if width - body.position.x < body.radius or body.position.x <= body.radius:
            body.velocity.x = -body.velocity.x
        if height - body.position.y < body.radius or body.position.y <= body.radius:
            body.velocity.y = -body.velocity.y

def bodies_collision(bodies):
    for i in range(len(bodies)):
            body = bodies[i]
            for j in range(i + 1, len(bodies)):
                next_body = bodies[j]
                body_distance = next_body.position - body.position
                body_distance_normalized = body_distance.normalize()
                if body_distance.length() <= body.radius + next_body.radius:
                    collide(body, next_body, body_distance_normalized, body_distance.length())
def move(bodies, dt):
    for body in bodies:
        body.position += body.velocity * dt

def physics_update(width, height, dt, bodies, G):
        handle_gravity(bodies, dt, G)
        move(bodies, dt)
        bodies_collision(bodies)
        wall_collision(width, height, bodies)
