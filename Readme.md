# Complicated

## What is Complciated?

Complicated is a simple app that lets you update your Apple Watch face complications
with WebHooks.

[![Complicated Watch Your Text Here](https://mikelyons.org/images/complicated/watch_your_message_250.png)](https://mikelyons.org/complicated)

[https://mikelyons.org/complicated](https://mikelyons.org/complicated)

[![Complicated Download App](https://mikelyons.org/images/complicated/download.png)](https://itunes.apple.com/us/app/complicated/id1444561091?ls=1&mt=8)

## How to install `complicated-python`

```
pip install complicated
```

## How to use the Complicated CLI tool

It's easy to update your Apple Watch Complications using the command line. The
command is just `complicated`, and you pass in API key, Complication type and
your new value in parenthesis

```
Usage: complicated <Complicated API Key> <complication type> "<New Value>"
Example:
complciated abcd1234 modularLarge "Hello World\nCan you see me"
```

Arguments:
 - `API Key`: You can get this from the settings page in the Complicated app
 - `Complication Type`: The complication that you want to update to the new value.
Here is a list of the available types: [ circularSmall, extraLarge, graphicBezel, graphicCorner, graphicRectangular, modularLarge, modularSmall, utilitarianLarge, utilitarianSmall ]
 - `New Value`: The new value to change the complciation to. Surround it with quotes if you want to include spaces. Use \n for new lines.


## How to use the Python Library

The python library is also dirt simple to use:

```python
from complicated import changeComplication

# Usage: changeComplication( '<api key>', '<complication type>', '<new value>' )
changeComplication( 'abcd1234', 'utilitarianSmall', 'new value' )
```
