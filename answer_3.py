mylst=[
    {
        "name":"abdullah",
        "phone":"05444444"
     
     },
        {
        "name":"mohammed",
        "phone":"43567"
     
     },
            {
        "name":"khalid",
        "phone":"12345"
     
     }
    
]

mylst.append(    {
        "name":"sultan",
        "phone":"676767676767"
     
     })

mylst[0].pop("name")
mylst[-1]["phone"] = "00009998877654"



print("key name exists in the first dict") if "name" in mylst[0] else print("key name doesn't exists in the first dict")