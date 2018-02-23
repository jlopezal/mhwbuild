import React, { Component } from "react";
import PropTypes from "prop-types";
import EquipmentSetCard from "../components/EquipmentSetCard";
import EquipmentPickerDialog from "../components/EquipmentPickerDialog";
import Button from "material-ui/Button";
import { withStyles } from "material-ui/styles";

import ShareIcon from "material-ui-icons/Share";

const styles = theme => ({
  buttonContainer: {
    display: "flex",
    justifyContent: "flex-end",
    marginTop: "16px"
  }
});

class Planner extends Component {
  constructor() {
    super();
    this.state = {
      set: {
        bonuses: {
          immediate: []
        },
        pieces: {}
      },
      setName: "Custom Set",
      dialogOpen: false,
      selectedPart: ""
    };
  }

  handlePartClick = part => {
    console.log(part);

    this.setState({ selectedPart: part, dialogOpen: true });
  };

  handlePieceSelected = piece => {
    this.setState({
      set: {
        ...this.state.set,
        pieces: {
          ...this.state.set.pieces,
          [piece.part]: piece
        }
      },
      dialogOpen: false
    });
  };

  handlePieceRemoved = piece => {
    const pieces = { ...this.state.set.pieces };
    delete pieces[piece];

    console.log(pieces);
    console.log(piece);

    this.setState({
      set: {
        ...this.state.set,
        pieces
      },
      dialogOpen: false
    });
  };

  render() {
    const { classes } = this.props;
    return (
      <div>
        <EquipmentSetCard
          set={this.state.set}
          title={this.state.setName}
          clickable={true}
          handlePartClick={this.handlePartClick}
        />
        <div className={classes.buttonContainer}>
          <Button color="primary">
            <ShareIcon />Share
          </Button>
        </div>
        <EquipmentPickerDialog
          open={this.state.dialogOpen}
          onClose={() => {
            this.setState({ dialogOpen: false });
          }}
          selectedPart={this.state.selectedPart}
          handlePieceSelected={this.handlePieceSelected}
          handlePieceRemoved={this.handlePieceRemoved}
        />
      </div>
    );
  }
}

Planner.propTypes = {};

export default withStyles(styles)(Planner);
