# Environmental Telemetry System Requirements

**Version:** 0.1  
**Status:** Preliminary

## 1. Project Objective

Design and build a portable, battery-powered environmental telemetry system capable of measuring environmental conditions, storing measurements locally, and transmitting telemetry wirelessly to a ground station.

The system will progress from a breadboard prototype to a custom PCB and will be used to develop practical skills in embedded systems, PCB design, RF communication, power management, firmware development, and engineering testing.

## 2. Preliminary System Requirements

### 2.1 Environmental Sensing

SEN-001: The system shall measure ambient temperature.

SEN-002: The system shall measure relative humidity.

SEN-003: The system shall measure atmospheric pressure.

SEN-004: The system shall measure air quality.

SEN-005: The system shall measure ultraviolet (UV) radiation.

### 2.2 Data Acquisition

DAQ-001: The system shall acquire and record environmental sensor measurements at an interval of 60 seconds during normal operation. 

### 2.3 Data Storage

DAT-001: The system shall store environmental measurements locally so that collected data remains available if wireless communication is interrupted.

DAT-002: Each stored measurement shall include a timestamp.

DAT-003: Each stored measurement shall include temperature, relative humidity, atmospheric pressure, air-quality, and UV measurements.

### 2.4 Power

PWR-001: The system shall operate continuously for a minimum of 24 hours on battery power under normal operating conditions.

PWR-002: The system shall monitor its battery voltage and include battery status in recorded telemetry.

### 2.5 Ground Station

COM-001: The system shall transmit environmental telemetry wirelessly to a ground station.

COM-002: The ground station shall receive telemetry and forward it to a computer over a wired interface.

COM-003: The computer shall display current telemetry values and historical data.

COM-004: The computer shall provide a local network interface that allows telemetry data to be viewed from a mobile device on the same network.

COM-005: The system shall target reliable wireless telemetry communication over a minimum distance of 500 meters with clear line of sight.

COM-006: Loss of wireless communication shall not prevent the remote station from continuing to collect and store environmental data.

COM-007: The system shall retain unsent telemetry records and transmit them after wireless communication is restored.

COM-008: Allow the computer/ground station to send commands back to the remote station.

### 2.6 Deployment

DEP-001: The remote station shall be portable and suitable for temporary outdoor deployment.

DEP-002: The enclosure shall protect electronics from normal outdoor environmental exposure while allowing the environmental sensors to obtain representative measurements of outside conditions.

DEP-003: The station shall support mounting near a window, on a suitable bracket, or in another temporary outdoor location.
