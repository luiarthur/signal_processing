package gui

import scalafx.Includes._
import scalafx.application.JFXApp
import scalafx.scene.Scene
import scalafx.scene.paint.Color._
import scalafx.scene.shape.Rectangle

// For Scatter Plot
// TODO: Left OFf Here.
// See: http://docs.oracle.com/javafx/2/charts/scatter-chart.htm
import javafx.scene.chart.NumberAxis;
import javafx.scene.chart.ScatterChart;
import javafx.scene.chart.XYChart;

object HelloStageDemo extends JFXApp {

  def rgb1(r:Double, g:Double, b:Double) = {
    require(r >= 0 && r <= 1)
    require(g >= 0 && g <= 1)
    require(b >= 0 && b <= 1)
    rgb((r*255).toInt, (g*255).toInt, (b*255).toInt)
  }

  stage = new JFXApp.PrimaryStage {
    title.value = "Hello Stage"
    width = 600
    height = 450
    scene = new Scene {
      fill = rgb1(.1, .1, .1)
      content = new Rectangle {
        x = 25
        y = 40
        width = 100
        height = 100
        fill <== when (hover) choose Grey otherwise Red
      }
    }
  }

  // TODO:
  // https://stackoverflow.com/questions/10121991/javafx-application-icon
  //stage.getIcons().add(new Image("file:icon.png"));
}

