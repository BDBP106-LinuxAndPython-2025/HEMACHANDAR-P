# use_json_processor.py
import q2 as jp

# Load JSON data
data = jp.load_json("players.json")

print(" Original JSON Data:")
jp.print_json(data)

# Update man_of_the_match
data = jp.update_man_of_the_match(data)

print("\n🏏 Updated JSON Data:")
jp.print_json(data)

# Write to a new file
jp.write_json("players_updated.json", data)
print("\n✅ Updated data written to players_updated.json")
