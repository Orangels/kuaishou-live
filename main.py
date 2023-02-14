import logging

from kuaishou import KsLive

if __name__ == '__main__':
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
    ks = KsLive.Tool()
    # ss='08a04e10828298ced230180520012a1b0a07582d426f67757312105273693578484a6f7859364a2f7636543a02706242a808086410a04e1a0c302e372e332d626574612e342200280330003a0e666562376331343a6d617374657242f102a206ed020a1d303a313a3130333437313539333530383a313033343731353933353038100118a48481d688ddbbbb6322407b226d656e74696f6e5f7573657273223a5b5d2c2261776554797065223a3730302c227269636854657874496e666f73223a5b5d2c2274657874223a2233227d2a150a11733a6d656e74696f6e65645f757365727312002a3b0a13733a636c69656e745f6d6573736167655f6964122465653931663962312d396165662d346566612d623631622d61336230373266383933373330073a81013248626877434843544d544d6c37366372416a6b57784f315a4749686f5a6341646e6337316567324a3268496746504454324e454c4f62354b39477446476a656a496b716657494e564b4458716d56334d4974337335766a554c5a74596d305246304551487a6261627a795548435643503770674a6a6c7a79484c6776364c6d69422465653931663962312d396165662d346566612d623631622d6133623037326638393337334a01305a09646f7579696e5f70637a130a0b73657373696f6e5f6169641204363338337a100a0b73657373696f6e5f6469641201307a150a086170705f6e616d651209646f7579696e5f70637a150a0f7072696f726974795f726567696f6e1202636e7a83010a0a757365725f6167656e7412754d6f7a696c6c612f352e3020284d6163696e746f73683b20496e74656c204d6163204f5320582031305f31355f3729204170706c655765624b69742f3533372e333620284b48544d4c2c206c696b65204765636b6f29204368726f6d652f3130382e302e302e30205361666172692f3533372e33367a160a0e636f6f6b69655f656e61626c65641204747275657a160a1062726f777365725f6c616e677561676512027a687a1c0a1062726f777365725f706c6174666f726d12084d6163496e74656c7a170a0c62726f777365725f6e616d6512074d6f7a696c6c617a80010a0f62726f777365725f76657273696f6e126d352e3020284d6163696e746f73683b20496e74656c204d6163204f5320582031305f31355f3729204170706c655765624b69742f3533372e333620284b48544d4c2c206c696b65204765636b6f29204368726f6d652f3130382e302e302e30205361666172692f3533372e33367a160a0e62726f777365725f6f6e6c696e651204747275657a140a0c73637265656e5f77696474681204313434307a140a0d73637265656e5f68656967687412033930307a0b0a077265666572657212007a1e0a0d74696d657a6f6e655f6e616d65120d417369612f5368616e676861697a0d0a0864657669636549641201307a1c0a057765626964121337313339333931353538393134333933363132900101aa010a646f7579696e5f776562b201077765625f73646b'
    # ks.hexStrToProtobuf(ss)
    c ='clientid=3; didv=1675056349580; userId=845495460; kuaishou.live.bfb1s=7206d814e5c089a58c910ed8bf52ace5; did=web_a41c846314016ca1a260444bb3c7d66c; client_key=65890b29; kpn=GAME_ZONE; _did=web_117262730815E9F7; kuaishou.live.web_st=ChRrdWFpc2hvdS5saXZlLndlYi5zdBKgAQkoEnsRiD0ovFwIQ828tvYMhmH6rThiUxM-uuTQtXKjmQEry1dCvI5sEsH9SZt9LNWcvJ_kNRPH2AFvS1awpa65z-Jpe3p2nbMvkpraiJV0WkJrvhLrCyb_CTCNPBGoYwUBaDoabrmZLqLJX-txGbrmUDIblQmR-MKwbPb7uQ5MszR2O3jaon_MtIrqnQA7e0IOBVmJT8N_p-lsiclN4NsaEsa__TMaP0jJgfAfW0kccZcKPyIgmgfFxb6YcCH2fKNK5CO2G4OWyK-WxFeXx6Bx8LA1FGcoBTAB; kuaishou.live.web_ph=8d652450751eaf1d2b61edf08b812bb0a41a; userId=845495460; ksliveShowClipTip=true'
    ks.init('https://live.kuaishou.com/u/3xeg79ue5ur4ayu', c)
    # ks.init('https://live.kuaishou.com/u/3xnkwrgq6wmkank', c)
    # 启动快手ws客户端
    ks.wssServerStart()