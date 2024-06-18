<!DOCTYPE html>
<html>
<head>
  <title>Ping Pong Game</title>
  <!-- Add the Bootstrap CSS file -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">

<!-- Add the Bootstrap JavaScript file -->


  <link rel="stylesheet" href="styles.css">
  <style>
    canvas {
      border: 1px solid black;
    }
  </style>
</head>
<body>
  <div class="container">
  <canvas id="canvas" width="600" height="400"></canvas>
</div>
<div class="button">
  <button id="start-btn" class="btn">Start</button>
    <button id="pause-btn" class="btn">Pause</button>
    <button id="restart-btn" class="btn">Restart</button>
  </div>
 <p class="control">Control: Player Left(W and S) | Player Right(↑ and ↓)</p>
  <!-- Add a modal element with an ID -->
<div class="modal" tabindex="-1" role="dialog" id="message-modal">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-body">
        <h5 id="message"></h5>
      </div>
      <div class="modal-footer">
        <button type="button" id="message-modal-close" class="btn btn-secondary" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>

  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
  <script src="script.js"></script>
</body>
</html>
