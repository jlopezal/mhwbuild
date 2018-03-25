import React, { Component } from "react";
import PropTypes from "prop-types";
import List, { ListItem, ListItemText } from "material-ui/List";
import Card, { CardContent } from "material-ui/Card";
import Typography from "material-ui/Typography";
import _ from "lodash";
import { observer } from "mobx-react";
import possibleSkills from "../data/skill";

const displaySkillTotal = skill => {
  let range = skill.level - possibleSkills[skill.name].levels.length;
  let style = {};
  if (range === 0) {
    style = { color: "#43A047" };
  } else if (range > 0) {
    style = { color: "#E53935" };
  } else {
    style = { color: "black" };
  }
  return (
    <div style={style}>{`${skill.name} ${skill.level}/${
      possibleSkills[skill.name].levels.length
    }`}</div>
  );
};

class SummaryCard extends Component {
  render() {
    const { set } = this.props;

    //iterate through set and get skills
    let totals = {};

    _.values(set.pieces).forEach(piece => {
      piece.skills.forEach(skill => {
        if (!totals[skill.name]) {
          totals[skill.name] = 0;
        }

        totals[skill.name] += skill.level;
      });
    });

    //iterate through decorations and get skills
    let decoParts = set.decorations;

    for (let part in decoParts) {
      if (decoParts.hasOwnProperty(part)) {
        let skills = decoParts[part];

        skills.forEach(skill => {
          //if no name, then empty
          if (!skill.name || skill.name === "") {
            return;
          }

          if (!totals[skill.skill]) {
            totals[skill.skill] = 0;
          }

          totals[skill.skill]++;
        });
      }
    }

    //skill.name for equipment, skill.skill for decoration
    let totalsArray = Object.keys(totals).map(function(skill) {
      return { name: skill, level: totals[skill] };
    });

    return (
      <div style={{ marginTop: 24 }}>
        <Card>
          <CardContent>
            <Typography variant="title">Summary</Typography>
            <Typography variant="subheading">
              <strong>Skill Totals</strong>
            </Typography>
            <List>
              {totalsArray.map(skill => {
                console.log(skill.name);
                return (
                  <ListItem key={skill.name} style={{ padding: "4px" }}>
                    <ListItemText primary={displaySkillTotal(skill)} />
                  </ListItem>
                );
              })}
            </List>
          </CardContent>
        </Card>
      </div>
    );
  }
}

SummaryCard.propTypes = {
  set: PropTypes.object
};

export default observer(SummaryCard);