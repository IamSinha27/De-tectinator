import React from 'react'
import {
    AppBar,
    Toolbar,
    Typography,
    Container,
    Grid,
    Card,
    CardContent,
    CardActions,
    CardMedia,
    Button,
  } from "@mui/material";

  import { Link } from 'react-router-dom';

function Home() {
  return (
    <div>
         <AppBar position="relative">
        <Toolbar>
          <h1>Detectinator</h1>
        </Toolbar>
      </AppBar>

      <main>
        <div>
          <Grid container padding="100px">
            <Grid item xs={12} lg={6}>
              <Typography
                styles={{ color: "black" }}
                variant="h2"
                align="center"
                color="black"
                // gutterBottom
              >
                LOGO
              </Typography>
            </Grid>

            <Grid item xs={12} lg={6}>
            Be it the challenging altitudes of Siachen, or the deep waters of the Indian oceans, our soldiers brave them all to secure our nation. One constant problem that hinders their call of duty, is the lack of efficient and quick respiratory healthcare testing and screening. Moreover, due to the extreme conditions and lack of proper infrastructure, a lot of precious time is wasted in the transport, storage and maintenance of the testing kits, tools and samples.
This is where our technology comes in. We have created a smart platform using AI which effectively detects and provides accurate results in respiratory diseases like the ongoing Covid-19, pneumonia and asthma. 
Soldiers will be able to easily access the platform and check for any such respiratory issues instantly.
            </Grid>
          </Grid>


          

          <div align="center">
            <Grid
              container
              spacing={2}
              justify="center"
              padding="100px"
              direction="row"
            >



            
              <Grid item key="1" xs={12} sm={6} md={4}>
                {/* card 1 */}
                <Card>
                  <CardMedia image="" title="Image Title" />
                  <CardContent>
                    <Typography gutterBottom variant="h5">
                      Asthma
                    </Typography>

                    <Typography>Description</Typography>
                  </CardContent>

                  <CardActions>
                    <Button size="small" color="primary">
                    <Link to="/asthma">Asthma</Link>


                    </Button>
                    
                  </CardActions>
                </Card>
              </Grid>
              {/* card 2 */}
              <Grid item key="2" xs={12} sm={6} md={4}>
                <Card>
                  <CardMedia
                    image="https://source.unsplash.com/random"
                    title="Image Title"
                  />
                  <CardContent>
                    <Typography gutterBottom variant="h5">
                      Covid
                    </Typography>

                    <Typography>Description</Typography>
                  </CardContent>

                  <CardActions>
                    <Button size="small" color="primary">
                    <Link to="/covid">Covid</Link>
                     Test
                    </Button>
                    
                  </CardActions>
                </Card>
              </Grid>

              {/* card 3 */}
              <Grid item key="3" xs={12} sm={6} md={4}>
                <Card>
                  <CardMedia
                    image="https://source.unsplash.com/random"
                    title="Image Title"
                  />
                  <CardContent>
                    <Typography gutterBottom variant="h5">
                      Pneumonia
                    </Typography>

                    <Typography>Description</Typography>
                  </CardContent>

                  <CardActions>
                    <Button size="small" color="primary">
                    <Link to="/pneumonia">Pneumonia</Link>
                      Test
                    </Button>
                    
                  </CardActions>
                </Card>
              </Grid>
            </Grid>
          </div>
        </div>
      </main>
    </div>
  )
}

export default Home;
