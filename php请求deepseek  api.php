<?php
$apiKey = "sk-9cd06806a978466a98ff5b3eb6cd6664";
$apiUrl = "https://api.deepseek.com/v1/chat/completions";

$headers = [
    'Content-Type: application/json',
    'Authorization: Bearer ' . $apiKey
];

$data = [
    'model' => 'deepseek-chat',  // 🎛️ 模型名称
    'messages' => [
        ['role' => 'user', 'content' => '你好呀~']
    ],
    'temperature' => 0.7  // 🌡️ 控制回答创意值
];

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $apiUrl);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
curl_close($ch);

// 🎉 解析AI回复
$result = json_decode($response, true);
echo $result['choices'][0]['message']['content'];
?>









