
def left_join(phrases: tuple) -> str:
    text = ",".join(phrases)
    text = text.replace('right', 'left')
    return text
    return ','.join(map(lambda x:x.replace('right','left'),phrases))


print("Example:")
print(left_join(("left", "right", "left", "stop")))

assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
assert left_join(("brightness wright",)) == "bleftness wleft"
assert left_join(("enough", "jokes")) == "enough,jokes"

print("The mission is done! Click 'Check Solution' to earn rewards!")