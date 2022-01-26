#!/usr/bin/python3

from gtts import gTTS
from playsound import playsound
from random import choice
from os import system
from termcolor import colored,cprint

system("clear"),print("\n","\t"*3,end=""),cprint("===>  ","white",attrs=["bold"],end=""),cprint("Please Turn Up The Volume","grey",attrs=["bold","blink"],end=""),cprint("   <===","white",attrs=["bold"],end="") ,print("\t"*4,end=""),cprint("####  ","white",attrs=["bold"],end=""),cprint("By : Abd Almoen Arafa (0.1Arafa)","yellow",attrs=["bold"],end=""),cprint("  ####","white",attrs=["bold"]),print("\t"*11,end=""),cprint("####  ","white",attrs=["bold"],end=""),cprint("Age : 15			      ","yellow",attrs=["bold"],end=""),cprint("	####","white",attrs=["bold"])
count,Count,counT=0,1,0
while Count > count:
	print("\t"*8,end=""),cprint("Your Points: ","blue",attrs=["bold"],end=""),cprint(counT,"green",attrs=["bold"]),cprint("[ ","grey",attrs=["bold"],end=""),cprint(count,"green",attrs=["bold"],end=""),cprint(" ]","grey",attrs=["bold"],end=" ")
	ask=input(colored("Do you want to start playing? (Enter or Y, N): ","blue",attrs=["bold"])).strip()
	if ask.lower() == "n" or ask.lower() == "no" or ask.lower() == "exit" or ask.lower() == "quit":   print("\n"),quit()
	else:
		text="name.no.yes.sure.happy.mode.gold.silver.paste.past.copy.move.movies.moon.can i get you the moon.was come on for you.car.window.metal.wood.turtle.lion.eagle.jaguar.shark.snake.block.tent.maybe.error.present.after.both.before.put.castle.bad guy.age.how much.it's a hard work.you always be my day one.don't really wanna die i just wanna feel alive.how long.how many.steam.stream.live.govern.about.long.this.around.play.by.these.those.this.at.now.own.give.look at me.life.nano.science.exit.quit.black screen.blue screen.white screen.park.part.party.pretty.pretty face.so much fun.each.approach.increase.ability.benefits.fit girl.fat girl.fit boy.fat boy.point.enter.star.stick.toxic.nine.has been.society.fuck society.thankful.apple.orange.i got you.did you get it.say hello for me.where are you from.how old are you.what's your name.do you like sciences.do you like the music.rockbye baby.don't cry please.just like this.it was the end.best movies.shorts.shoes.the end.you're my day one.come and smell this flower.i'll eat this.are you here.is she there.hello,how are you today.are you okay.don't look at me like this.it's a bad feelings.it's your cat or what.i'm going to my home.wide pool.world wide.nice tree.around the world.all over the world.come here boy.come here girl.what's your favourite color.peace out.rest in peace.it's a nice car.purple car.green car.hot wheels.turkey.england.syria.egypt.algeria.america.colombia.germany.africa.middle east.canada.moroco.lebanon.iraq.middle east servers.europe.open this file.heaven.darkest day.give me the loop.high performance.large icon.low battery.don't run away.look at me.locked phone.hard battle.nice game.thug life.a lot of money.there is a cd there.the floor is too long.what is your language.i like this wall.let's make some noise.beautiful table.she's the tallest woman.are you there.bodybuilding is dangerous when playing fault.stop please.read this.turn off this computer.turn on the ps4.her hair is too long.she's a blonde woman.blue eyes.let's play together on this phone.don't run while the weather is stormy.it was a hard day.just read this.study for your test.you just want attention.trust me.can i get you the moon.sunshine.machine.application.exciting challenge.let's go.i don't know.i know it.i swear to god.animal.generator.purple.what the fuck.may i help you.can i see you.click here.this is for test.how are you.is that you.how old are you.ok thank you.come on over in my direction.isn't lovely all alone.baby don't leave me.begginer.are you a human.i think he's right.ok peace.see you later.i can't hold on.i'm waiting for you.hang on.please don't break my heart.he's a boy.boy.she's a girl.girl.maths.numbers.are you alone.bullshit.you're right.fault.alive.can you hate me.i love you.my mom.i love that.sky.the sky is high.key.robot.dark.high building.weight.password.email.raise of nations.general.computer.are you a child.children.television.one hundred.thousands of people.lover.i can't wait for it.control.touchpad.character.mother.father.son.family.daughter.cousin.grandmother.grandfather.nice body.cute one.he's a tall man.i like him.i like her.is she need me.need is need.fire.sing with me.what is the best song for you.singer.female.male.make.made.cooking.my mom's cooking a nice food.cheese.meeting.mate.university.school.primary school.dog.cat.turtle.airplane.telephone.house.uniform.notebook.book.horor.pencil.afraid.changes.i won't let you go.let me love you.kill the monster.don't play this game again.do you wanna come with me.yes write this.no man i don't like it.under the sea.brown skin.white leather.let's drink this.are you ready.refresh.guide book.restaurant.sort by.view.quickly please.nice clothes.hot food.spicy food.deep sea.adult man.adult woman.oldman.oldwomen.group of youngs.baby you can hold me.bettery.charger.telephone.light.motion.easly.fast.create.chat.zoom.zoo.input.output.display.desktop.launcher.join us.call me later.as tall as.meeting.angry.after.again.also.against.area.baby.away.bad.bag.boy.agency.although.above.about.add.address.affect.administrator.hungry.east.west.south.north.different.island.fairly.juice.kiss.knife.rain.bury.damage.umbrella.violent.wire.worth.worst.ugly.teach.learn.safe.safely.rainbow.library.cartoon.network.awesome.huge.healthy.handsome.gentle.delicious.energy.famous.family.farm.from.camera.careful.carefully.attractive.bigger.fitter.but".split(".")
		main_text=choice(text)
		speaker=gTTS(text=main_text, lang="en")
		speaker.save("welcome.mp3"),playsound("welcome.mp3")
		ask=input(colored("Enter the Text: ","blue",attrs=["bold"])).strip()
		if ask.lower() == main_text:
			cprint("True ;)","cyan",attrs=["bold"],end="\n")
			counT+=1
		elif ask.lower() == "n":   print("\n"),quit()
		else:
			cprint("False :( , it's:","red",attrs=["bold"],end=" "),cprint(main_text,"magenta",attrs=["bold"])
			counT-=1
		count+=1
		Count+=1
#By : Abd Almoen Arafa (0.1Arafa)
#Age : 15
