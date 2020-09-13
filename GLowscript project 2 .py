GlowScript 2.9 VPython

# Names: Ackeem Greene, Kevin Davis and Semeion Stafford
# Course: Cmps 4559
# Date: Oct/24/2019
# Description: This program simulates a Our solar system
 and its reaction to the forces created by celestial bodies.


scene.width = 1500
scene.height = 800  
#scene.background = black
scene.ambient = color.gray(0.1)
scene.forward = vec(0.3,0.9,0.6)





def force(planet1,planet2):
    # Calculate the gravitational force on planet1 by pplanet2.
    G = 1 
    # Calculate distance vector between planet1 and planet2.
    r_vec = planet1.pos-planet2.pos
    # Calculate magnitude of distance vector.
    r_mag = mag(r_vec)
    # Calcualte unit vector of distance vector.
    r_hat = r_vec/r_mag
    # Calculate force magnitude.
    force_mag = G*planet1.mass*planet2.mass/r_mag**2
    # Calculate force vector.
    force_vec = -force_mag*r_hat
    return force_vec
    

#planet creation
    
sun = sphere( pos=vector(0,0,0), radius=0.25,
               mass = 1.0*1000, momentum=vector(0,0,0),  make_trail=True, emissive=True, texture="https://images.designtrends.com/wp-content/uploads/2016/08/21193332/f66.jpg")
               

sunlight2 = local_light(pos=sun.pos,color=color.gray(0.9))
               
               
mercury = sphere( pos=vector(0.4,0,0), radius=0.04, mass = 0.62, momentum=vector(0,30,0), texture="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/e0763947-6f42-4d09-944f-c2d6f41c415b/dcaig77-18800e1e-24aa-43e5-9dd0-3dff9bcf8d0c.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2UwNzYzOTQ3LTZmNDItNGQwOS05NDRmLWMyZDZmNDFjNDE1YlwvZGNhaWc3Ny0xODgwMGUxZS0yNGFhLTQzZTUtOWRkMC0zZGZmOWJjZjhkMGMuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.TLHMNUPdW5unEpvHhX2wn8iRLpHN15hcMvFLWtmXWyE" )
               
venus = sphere( pos=vector(0.6,0,0), radius=0.07, mass = 0.77, momentum=vector(0,30,0), retain=50, texture="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/90ad8232-4e09-4675-b9e7-bc2898960870/dc0ss1u-9ce1cbd0-6f56-4bb1-ab24-e64089914504.png/v1/fill/w_1024,h_512,q_80,strp/venus_cloud_texture_map_by_jcpag2010_dc0ss1u-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NTEyIiwicGF0aCI6IlwvZlwvOTBhZDgyMzItNGUwOS00Njc1LWI5ZTctYmMyODk4OTYwODcwXC9kYzBzczF1LTljZTFjYmQwLTZmNTYtNGJiMS1hYjI0LWU2NDA4OTkxNDUwNC5wbmciLCJ3aWR0aCI6Ijw9MTAyNCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.W_cmzd6frwnuf_p4_K40ME9cIai41bgUtrIImysmwaM" )
               
earth = sphere( pos=vector(0.8,0,0), radius=0.06, mass = 0.9, momentum=vector(0,30,0), texture="https://live.staticflickr.com/2521/3884071286_edb50f8137_b.jpg" )
               
mars = sphere( pos=vector(1,0,0), radius=0.05, mass = 1, momentum=vector(0,30,0),texture="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/6e527eb9-99dc-4554-9ea2-dd0e84e79860/dckiu8c-727ad23f-7760-42f2-9669-aa2de0f3c832.png/v1/fill/w_1264,h_632,q_70,strp/mars_texture_map_used_by_solar_walk_2_by_bob3studios_dckiu8c-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTAyNCIsInBhdGgiOiJcL2ZcLzZlNTI3ZWI5LTk5ZGMtNDU1NC05ZWEyLWRkMGU4NGU3OTg2MFwvZGNraXU4Yy03MjdhZDIzZi03NzYwLTQyZjItOTY2OS1hYTJkZTBmM2M4MzIucG5nIiwid2lkdGgiOiI8PTIwNDgifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.dRnTFnFlXIE0q0TzB3phykHWs_Ev0yRSN4gEW7vG8mU")
               
jupiter = sphere( pos=vector(1.2,0,0), radius=0.08, mass = 1.1, momentum=vector(0,30,0), texture="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/06a094a4-7bd7-4bb9-b998-6c1e17f66c08/db8yfsl-a3c9000a-af5e-4d9a-8414-b316dd81f4c8.png/v1/fill/w_1024,h_512,q_80,strp/jupiter_true_color_texture_map___juno__hubble__16__by_fargetanik_db8yfsl-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NTEyIiwicGF0aCI6IlwvZlwvMDZhMDk0YTQtN2JkNy00YmI5LWI5OTgtNmMxZTE3ZjY2YzA4XC9kYjh5ZnNsLWEzYzkwMDBhLWFmNWUtNGQ5YS04NDE0LWIzMTZkZDgxZjRjOC5wbmciLCJ3aWR0aCI6Ijw9MTAyNCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.NuRE13CW0DHfsYJWpxsaqzS7qo6f1S5GhfD89NlhwXs")
               
saturn = sphere( pos=vector(1.4,0,0), radius=0.07, mass = 1.19, momentum=vector(0,30,0), texture="data:image/jpeg;base64,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")
   
satRing = ring( pos=saturn.pos, axis=vec(0.0,0.0,2), size=vec(0.01,0.20,0.20), color=color.yellow)
    
uranus = sphere( pos=vector(1.6,0,0), radius=0.04, mass = 1.25, momentum=vector(0,30,0), texture="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxAPDQ0NDRAPDw0NDQ0NDQ0NDxAPDQ0NFREWFhURFRMYHSggGBolGxUVITEhJSkrLi4uFx8zODM4NygtLisBCgoKDg0NDg0NFSsZFR0tLSs3LSsrKysrLSstKysrKzcrKysrNy0tKysrKysrKysrKzcrLSsrKysrKysrKystK//AABEIAJ8BPgMBIgACEQEDEQH/xAAZAAADAQEBAAAAAAAAAAAAAAAAAQIDBAf/xAAnEAEAAwABAgUFAQEBAAAAAAAAARESAhRhBCFRcfADE0GBkaHBMf/EABkBAQEBAAMAAAAAAAAAAAAAAAABAgMEBf/EABcRAQEBAQAAAAAAAAAAAAAAAAAREgH/2gAMAwEAAhEDEQA/APRqFKoU7Lz00KUARQpYCJoqXQCIoUuhQRFHSqFBE0KVQoImhShQRNClUKCJoUoUETQpVAImipYCIo6UKBFHlVAE0VLARNClUKCJoUqhQJoUqhQRNClCgiaFKoUBk1wMI1GYaYGAjMU0wMAzFNMlkIigvB4CMw0wWAQF4GARQXgYBAXg8AzoU0wMBGYaYGAjINcDARkbTAwEZk1wMBGQa4GAZhpgYCMw0wMBGYaYGAjMNMDARkGuBgI1Dk6ifkj78+kmV1x1jycnU+5T4rtJk3x2+ReTj6oR4oyb47A4+qPqO8f0yb46w458V8gR4lc9N8dhuLqinxZnpvjtoOKPFn1aZ6b47A4urOPFLnpvjsDk6guoTJrjsHk458QOpM9N8dnkHH1J/f8AQyb467PycX3x1Bk3x2WLcfUlHiTJvjts3F1Jx4mDK7467Dk6mBHioMm+OsOSfE9y6nuZTfHZZ24ep7jqTJvju8i8nFHih1S5N8dw8nD1Y6oyb47fIOSPEFPiflpk3xxa9xv3Y2Lc0cFbbGoY2LCtdQNQysWFbajuNwxsWDfcDcMCCujceo1DnFkK33BbjuxEEK21AuO7KxZCttQNQys9EK1jnHoNx6MtDRCtJ5R6CebLRWQrbXuWvdloaCtdQccoY2LCtp5QNQxsWQraOUHHKGFiyFdXL6vGqqGc8oY2VkK2uBcfIZWLCtrFwxs7CtLg7juysTJCtbgX7sbFkKQaxxgfbEZG0n6ZYBFBeCngCTs8nkRNkvAwKgKyeVGYa4L7aCAuPpq+0DINJ+mWAQdKwWe4JkLwWQSFYPAICsHHEEE1zAn6SkZWGv2hP0kIyM8DIEFUdAgLwdAzDTMFgGdi2lCgZzzEc+7KwrNbbn1GpY2NSFb6ktyx0Wgrbc9h9yWNnYlbxz9j1Lns9SLW+pLTHUloK2nlJ8fqSwsrCuvclPKezmjlJ7kK6J5Smec9mO5K5CtvuSU859WVyLErXU+p8eUsbFi10XIufVhqS0hW2u5allotKVtuTj6jCxYldOhqXNcjUi1vPOU7llckJW2j+5LCxYV0fcG5YxyGha21J6n1YbLQVtuT2wiTsKmysSmhF2J5IoV+LBWxaMHHEIqztIoIqztNAIdi0mEURCgh2UzPsBQQaTPM6k8yKUc5OxkZCCxYyMiHZWI49hUhDsrKjyEFiyoQEVZWcNInj+bCMrDac+s/sr4hGItrznj+GUhBY0lUcZn0AWIkq9jiAOzsjvsAoLop4s1uIoV2n+ryI4hEQa4juPP1n+yUiZ+eR8Y7/wCSdephEz7x/JOI9v8AT+fgUEKhS4gT+hYmipf8KgiVxy7Cj4iRPLtBRK+SaCF/FZ9v9FAWFPEl/soKkKIgp4qkFIieIz8tYCM44xf/AJE/s54x+Ij5+1UKCIjj7f0V8uFUMwETRU0iBMBGVBpPEqKRFFlpQpaRnHGfRURPyYPlx7COBSFXzyEx88lRxGfZKRVewoGjRZKIUViHVlQqToUpj1I7FqCIOYTY0BgrAK8ymU2qJ+UgLFpmRoFWRD9wBiysWodiJIAqflSVF/gQVAKy81FRAn+/qSjjJzFICvYrkBRUELEX+AOIFen/AA6kkCkRB2FCFKz7f0q9v6BUI4mVAqhQACipQAk0sAnJZXQpBFClUMgmhSsilE0DyeUE0WV5GVEUTTIygz/RryMgigvIyCKOlZGQSFZGQRYXkZUQasnlBEQuJFCgEyQACSOjpQoiDqBQpAslSqKYUf/Z")
               
neptune = sphere( pos=vector(1.8,0,0), radius=0.05, mass = 1.3, momentum=vector(0,30,0), texture="data:image/jpeg;base64,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" )
               
pluto = sphere( pos=vector(2,0,0), radius=0.05, mass = 1.35, momentum=vector(0,30,0), texture="data:image/jpeg;base64,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")
               
             

dt = 0.0001
t = 0
while (True):
    rate(100)
    
     #sun's  force is affected by all the planets
    sun.force = force(sun,mercury)  + force(sun,venus) + force(sun,earth) + force(sun,mars) + force(sun,jupiter) + force(sun,saturn) + force(sun,uranus) + force(sun,neptune) + force(sun,pluto)
    earth.force = force(earth,sun)
    
    #venus sun
    venus.force = force(venus,sun)
    
    mercury.force = force(mercury,sun)
    
    mars.force = force(mars,sun)
    
    jupiter.force = force(jupiter,sun)
    
    saturn.force = force(saturn,sun)
    
    uranus.force = force(uranus,sun)
    
    neptune.force = force(neptune,sun)
    
    pluto.force = force(pluto,sun)
    
  #***********************************************************************************  
    sun.momentum = sun.momentum + sun.force*dt
   
    mercury.momentum = mercury.momentum + mercury.force*dt
    venus.momentum = venus.momentum + venus.force*dt
    earth.momentum = earth.momentum + earth.force*dt
    mars.momentum = mars.momentum + mars.force*dt
    jupiter.momentum = jupiter.momentum + jupiter.force*dt
    saturn.momentum = saturn.momentum + saturn.force*dt
    uranus.momentum = uranus.momentum + uranus.force*dt
    neptune.momentum = neptune.momentum + neptune.force*dt
    pluto.momentum = pluto.momentum + pluto.force*dt
   
   
 #************************************************************************************  
    #update positions
    sun.pos = sun.pos + sun.momentum/sun.mass*dt
    
    venus.pos = venus.pos + venus.momentum/venus.mass*dt
    mercury.pos = mercury.pos + mercury.momentum/mercury.mass*dt
    earth.pos = earth.pos + earth.momentum/earth.mass*dt
    mars.pos = mars.pos + mars.momentum/mars.mass*dt
    jupiter.pos = jupiter.pos + jupiter.momentum/jupiter.mass*dt
    saturn.pos = saturn.pos + saturn.momentum/saturn.mass*dt
    satRing.pos = saturn.pos
    uranus.pos = uranus.pos + uranus.momentum/uranus.mass*dt
    neptune.pos = neptune.pos + neptune.momentum/neptune.mass*dt
    pluto.pos = pluto.pos + pluto.momentum/pluto.mass*dt
    
    
    t = t + dt
