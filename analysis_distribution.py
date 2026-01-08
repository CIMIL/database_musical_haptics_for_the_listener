import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt


infile = "database_musical_haptics_for_the_listener.csv"


df = pd.read_csv(infile, keep_default_na=False)   # preserve textual 'NA' as string)


# Extract the columns
col_year                    = df["year"]
col_wearability             = df["wearability"]
col_presentation_mode       = df["presentation_mode"]
col_deployment_context      = df["deployment_context"]
col_form_factor             = df["form_factor"]
col_target_body_area        = df["target_body_area"]
col_stimulation_scope       = df["stimulation_scope"]
col_stimulus_type           = df["stimulus_type"]
col_actuator_type           = df["actuator_type"]
col_audio_tactile_mapping   = df["audio-tactile_mapping"]
col_audio_device            = df["audio_device"]
col_accessibility_focus     = df["accessibility_focus"]
col_connectivity            = df["connectivity"]
col_application_domain      = df["application_domain"]
	


##############################################################
# purpose split by accessibility_focus
purpose_counts = {}

for _, row in df.iterrows():
    entry = row["purpose"]
    focus = row["accessibility_focus"]

    if pd.isna(entry) or focus not in ["no", "DHH"]:
        continue

    items = [x.strip() for x in entry.replace(',', ';').split(';') if x.strip()]

    for item in items:
        if item not in purpose_counts:
            purpose_counts[item] = {"no": 0, "DHH": 0}

        purpose_counts[item][focus] += 1

# Sort by total count (no + DHH)
purpose_counts_sorted = dict(
    sorted(
        purpose_counts.items(),
        key=lambda x: x[1]["no"] + x[1]["DHH"],
        reverse=True
    )
)

# Print results
print("\n" + 20 * "#" + " purpose " + "\n")
for k, v in purpose_counts_sorted.items():
    total = v["no"] + v["DHH"]
    print(f"{k}: total={total}, no={v['no']}, DHH={v['DHH']}")



##############################################################
# wearability split by accessibility_focus
wearability_counts = {}

for _, row in df.iterrows():
    entry = row["wearability"]
    focus = row["accessibility_focus"]

    if pd.isna(entry) or focus not in ["no", "DHH"]:
        continue

    items = [x.strip() for x in entry.replace(',', ';').split(';') if x.strip()]

    for item in items:
        if item not in wearability_counts:
            wearability_counts[item] = {"no": 0, "DHH": 0}

        wearability_counts[item][focus] += 1

# Sort by total count (no + DHH)
wearability_counts_sorted = dict(
    sorted(
        wearability_counts.items(),
        key=lambda x: x[1]["no"] + x[1]["DHH"],
        reverse=True
    )
)

# Print results
print("\n" + 20 * "#" + " wearability " + "\n")
for k, v in wearability_counts_sorted.items():
    total = v["no"] + v["DHH"]
    print(f"{k}: total={total}, no={v['no']}, DHH={v['DHH']}")

##############################################################
# presentation_mode split by accessibility_focus
presentation_mode_counts = {}

for _, row in df.iterrows():
    entry = row["presentation_mode"]
    focus = row["accessibility_focus"]

    if pd.isna(entry) or focus not in ["no", "DHH"]:
        continue

    items = [x.strip() for x in entry.replace(',', ';').split(';') if x.strip()]

    for item in items:
        if item not in presentation_mode_counts:
            presentation_mode_counts[item] = {"no": 0, "DHH": 0}

        presentation_mode_counts[item][focus] += 1

# Sort by total count (no + DHH)
presentation_mode_counts_sorted = dict(
    sorted(
        presentation_mode_counts.items(),
        key=lambda x: x[1]["no"] + x[1]["DHH"],
        reverse=True
    )
)

# Print results
print("\n" + 20 * "#" + " presentation_mode " + "\n")
for k, v in presentation_mode_counts_sorted.items():
    total = v["no"] + v["DHH"]
    print(f"{k}: total={total}, no={v['no']}, DHH={v['DHH']}")

##############################################################
# deployment_context split by accessibility_focus
deployment_context_counts = {}

for _, row in df.iterrows():
    entry = row["deployment_context"]
    focus = row["accessibility_focus"]

    if pd.isna(entry) or focus not in ["no", "DHH"]:
        continue

    items = [x.strip() for x in entry.replace(',', ';').split(';') if x.strip()]

    for item in items:
        if item not in deployment_context_counts:
            deployment_context_counts[item] = {"no": 0, "DHH": 0}

        deployment_context_counts[item][focus] += 1

# Sort by total count (no + DHH)
deployment_context_counts_sorted = dict(
    sorted(
        deployment_context_counts.items(),
        key=lambda x: x[1]["no"] + x[1]["DHH"],
        reverse=True
    )
)

# Print results
print("\n" + 20 * "#" + " deployment_context " + "\n")
for k, v in deployment_context_counts_sorted.items():
    total = v["no"] + v["DHH"]
    print(f"{k}: total={total}, no={v['no']}, DHH={v['DHH']}")

##############################################################
# form_factor split by accessibility_focus
form_factor_counts = {}

for _, row in df.iterrows():
    entry = row["form_factor"]
    focus = row["accessibility_focus"]

    if pd.isna(entry) or focus not in ["no", "DHH"]:
        continue

    items = [x.strip() for x in entry.replace(',', ';').split(';') if x.strip()]

    for item in items:
        if item not in form_factor_counts:
            form_factor_counts[item] = {"no": 0, "DHH": 0}

        form_factor_counts[item][focus] += 1

# Sort by total count (no + DHH)
form_factor_counts_sorted = dict(
    sorted(
        form_factor_counts.items(),
        key=lambda x: x[1]["no"] + x[1]["DHH"],
        reverse=True
    )
)

# Print results
print("\n" + 20 * "#" + " form_factor " + "\n")
for k, v in form_factor_counts_sorted.items():
    total = v["no"] + v["DHH"]
    print(f"{k}: total={total}, no={v['no']}, DHH={v['DHH']}")


##############################################################
# target_body_area split by accessibility_focus
target_body_area_counts = {}

for _, row in df.iterrows():
    entry = row["target_body_area"]
    focus = row["accessibility_focus"]

    if pd.isna(entry) or focus not in ["no", "DHH"]:
        continue

    items = [x.strip() for x in entry.replace(',', ';').split(';') if x.strip()]

    for item in items:
        if item not in target_body_area_counts:
            target_body_area_counts[item] = {"no": 0, "DHH": 0}

        target_body_area_counts[item][focus] += 1

# Sort by total count (no + DHH)
target_body_area_counts_sorted = dict(
    sorted(
        target_body_area_counts.items(),
        key=lambda x: x[1]["no"] + x[1]["DHH"],
        reverse=True
    )
)

# Print results
print("\n" + 20 * "#" + " target_body_area " + "\n")
for k, v in target_body_area_counts_sorted.items():
    total = v["no"] + v["DHH"]
    print(f"{k}: total={total}, no={v['no']}, DHH={v['DHH']}")

##############################################################
# stimulation_scope split by accessibility_focus
stimulation_scope_counts = {}

for _, row in df.iterrows():
    entry = row["stimulation_scope"]
    focus = row["accessibility_focus"]

    if pd.isna(entry) or focus not in ["no", "DHH"]:
        continue

    items = [x.strip() for x in entry.replace(',', ';').split(';') if x.strip()]

    for item in items:
        if item not in stimulation_scope_counts:
            stimulation_scope_counts[item] = {"no": 0, "DHH": 0}

        stimulation_scope_counts[item][focus] += 1

# Sort by total count (no + DHH)
stimulation_scope_counts_sorted = dict(
    sorted(
        stimulation_scope_counts.items(),
        key=lambda x: x[1]["no"] + x[1]["DHH"],
        reverse=True
    )
)

# Print results
print("\n" + 20 * "#" + " stimulation_scope " + "\n")
for k, v in stimulation_scope_counts_sorted.items():
    total = v["no"] + v["DHH"]
    print(f"{k}: total={total}, no={v['no']}, DHH={v['DHH']}")

##############################################################
# stimulus_type split by accessibility_focus
stimulus_type_counts = {}

for _, row in df.iterrows():
    entry = row["stimulus_type"]
    focus = row["accessibility_focus"]

    if pd.isna(entry) or focus not in ["no", "DHH"]:
        continue

    items = [x.strip() for x in entry.replace(',', ';').split(';') if x.strip()]

    for item in items:
        if item not in stimulus_type_counts:
            stimulus_type_counts[item] = {"no": 0, "DHH": 0}

        stimulus_type_counts[item][focus] += 1

# Sort by total count (no + DHH)
stimulus_type_counts_sorted = dict(
    sorted(
        stimulus_type_counts.items(),
        key=lambda x: x[1]["no"] + x[1]["DHH"],
        reverse=True
    )
)

# Print results
print("\n" + 20 * "#" + " stimulus_type " + "\n")
for k, v in stimulus_type_counts_sorted.items():
    total = v["no"] + v["DHH"]
    print(f"{k}: total={total}, no={v['no']}, DHH={v['DHH']}")
    


##############################################################
# actuator_type split by accessibility_focus
actuator_type_counts = {}

for _, row in df.iterrows():
    entry = row["actuator_type"]
    focus = row["accessibility_focus"]

    if pd.isna(entry) or focus not in ["no", "DHH"]:
        continue

    items = [x.strip() for x in entry.replace(',', ';').split(';') if x.strip()]

    for item in items:
        if item not in actuator_type_counts:
            actuator_type_counts[item] = {"no": 0, "DHH": 0}

        actuator_type_counts[item][focus] += 1

# Sort by total count (no + DHH)
actuator_type_counts_sorted = dict(
    sorted(
        actuator_type_counts.items(),
        key=lambda x: x[1]["no"] + x[1]["DHH"],
        reverse=True
    )
)

# Print results
print("\n" + 20 * "#" + " actuator_type " + "\n")
for k, v in actuator_type_counts_sorted.items():
    total = v["no"] + v["DHH"]
    print(f"{k}: total={total}, no={v['no']}, DHH={v['DHH']}")


##############################################################
# audio_tactile_mapping split by accessibility_focus
audio_tactile_mapping_counts = {}

for _, row in df.iterrows():
    entry = row["audio-tactile_mapping"]
    focus = row["accessibility_focus"]

    if pd.isna(entry) or focus not in ["no", "DHH"]:
        continue

    items = [x.strip() for x in entry.replace(',', ';').split(';') if x.strip()]

    for item in items:
        if item not in audio_tactile_mapping_counts:
            audio_tactile_mapping_counts[item] = {"no": 0, "DHH": 0}

        audio_tactile_mapping_counts[item][focus] += 1

# Sort by total count (no + DHH)
audio_tactile_mapping_counts_sorted = dict(
    sorted(
        audio_tactile_mapping_counts.items(),
        key=lambda x: x[1]["no"] + x[1]["DHH"],
        reverse=True
    )
)

# Print results
print("\n" + 20 * "#" + " audio_tactile_mapping " + "\n")
for k, v in audio_tactile_mapping_counts_sorted.items():
    total = v["no"] + v["DHH"]
    print(f"{k}: total={total}, no={v['no']}, DHH={v['DHH']}")


##############################################################
# audio_device split by accessibility_focus
audio_device_counts = {}

for _, row in df.iterrows():
    entry = row["audio_device"]
    focus = row["accessibility_focus"]

    if pd.isna(entry) or focus not in ["no", "DHH"]:
        continue

    items = [x.strip() for x in entry.replace(',', ';').split(';') if x.strip()]

    for item in items:
        if item not in audio_device_counts:
            audio_device_counts[item] = {"no": 0, "DHH": 0}

        audio_device_counts[item][focus] += 1

# Sort by total count (no + DHH)
audio_device_counts_sorted = dict(
    sorted(
        audio_device_counts.items(),
        key=lambda x: x[1]["no"] + x[1]["DHH"],
        reverse=True
    )
)

# Print results
print("\n" + 20 * "#" + " audio_device " + "\n")
for k, v in audio_device_counts_sorted.items():
    total = v["no"] + v["DHH"]
    print(f"{k}: total={total}, no={v['no']}, DHH={v['DHH']}")



##############################################################
#accessibility_focus
accessibility_focus_counts = {}

for entry in col_accessibility_focus:
    # Split on common separators (adjust if needed)
    items = [x.strip() for x in entry.replace(',', ';').split(';') if x.strip()]

    for item in items:
        accessibility_focus_counts[item] = accessibility_focus_counts.get(item, 0) + 1

# Sort by descending count
accessibility_focus_counts_sorted = dict(sorted(accessibility_focus_counts.items(), key=lambda x: x[1], reverse=True))

# Print results
print("\n" +  20*"#" + "accessibility_focus" + "\n")
for k, v in accessibility_focus_counts_sorted.items():
    print(f"{k}: {v}")



##############################################################
# connectivity split by accessibility_focus
connectivity_counts = {}

for _, row in df.iterrows():
    entry = row["connectivity"]
    focus = row["accessibility_focus"]

    if pd.isna(entry) or focus not in ["no", "DHH"]:
        continue

    items = [x.strip() for x in entry.replace(',', ';').split(';') if x.strip()]

    for item in items:
        if item not in connectivity_counts:
            connectivity_counts[item] = {"no": 0, "DHH": 0}

        connectivity_counts[item][focus] += 1

# Sort by total count (no + DHH)
connectivity_counts_sorted = dict(
    sorted(
        connectivity_counts.items(),
        key=lambda x: x[1]["no"] + x[1]["DHH"],
        reverse=True
    )
)

# Print results
print("\n" + 20 * "#" + " connectivity " + "\n")
for k, v in connectivity_counts_sorted.items():
    total = v["no"] + v["DHH"]
    print(f"{k}: total={total}, no={v['no']}, DHH={v['DHH']}")



##############################################################
# application_domain split by accessibility_focus
application_domain_counts = {}

for _, row in df.iterrows():
    entry = row["application_domain"]
    focus = row["accessibility_focus"]

    if pd.isna(entry) or focus not in ["no", "DHH"]:
        continue

    items = [x.strip() for x in entry.replace(',', ';').split(';') if x.strip()]

    for item in items:
        if item not in application_domain_counts:
            application_domain_counts[item] = {"no": 0, "DHH": 0}

        application_domain_counts[item][focus] += 1

# Sort by total count (no + DHH)
application_domain_counts_sorted = dict(
    sorted(
        application_domain_counts.items(),
        key=lambda x: x[1]["no"] + x[1]["DHH"],
        reverse=True
    )
)

# Print results
print("\n" + 20 * "#" + " application_domain " + "\n")
for k, v in application_domain_counts_sorted.items():
    total = v["no"] + v["DHH"]
    print(f"{k}: total={total}, no={v['no']}, DHH={v['DHH']}")



##############################################################
#year
# Count occurrences
year_counts = col_year.value_counts().to_dict()
#filter between 2003 and 2025
year_counts = dict([item for item in year_counts.items() if 2003 <= item[0] <= 2025])


# Sort by ascending year
year_counts_sorted = dict(sorted(year_counts.items(), key=lambda x: x[0], reverse=False))

# Print results
print("\n" +  20*"#" + "year" + "\n")
for year, count in year_counts_sorted.items():
    print(f"{year}: {count}")


# Print total number of entries
#total = sum(year_counts_sorted.values())
#print("\nTotal:", total)

##############################################################


# Count total papers per year
total_counts = col_year.value_counts().to_dict()

# Count papers per year with accessibility_focus == "no"
no_counts = df[df["accessibility_focus"] == "no"]["year"].value_counts().to_dict()

# Count papers per year with accessibility_focus == "DHH"
dhh_counts = df[df["accessibility_focus"] == "DHH"]["year"].value_counts().to_dict()

# Filter years 2003–2025 and sort
def filter_and_sort(d):
    return dict(sorted(
        [(y, c) for y, c in d.items() if 2003 <= y <= 2025],
        key=lambda x: x[0]
    ))

total_counts = filter_and_sort(total_counts)
no_counts = filter_and_sort(no_counts)
dhh_counts = filter_and_sort(dhh_counts)


# Plot
plt.figure(figsize=(8, 5))
plt.plot(total_counts.keys(), total_counts.values(), color="black", label="Total")
plt.plot(no_counts.keys(), no_counts.values(), color="red", linestyle="--", label="No accessibility focus")
plt.plot(dhh_counts.keys(), dhh_counts.values(), color="blue", linestyle=":", label="DHH focus")
plt.xlabel("Year", fontsize=15)
plt.ylabel("Number of papers", fontsize=15)
plt.xticks(range(2003, 2026, 2))
plt.xticks(rotation=45)
plt.xlim(2003, 2025)
plt.ylim(0, 20)
plt.yticks(range(0, 23, 2))
plt.legend()
plt.tight_layout()
plt.savefig("historical_distribution.png", dpi=300, bbox_inches='tight')
plt.show()