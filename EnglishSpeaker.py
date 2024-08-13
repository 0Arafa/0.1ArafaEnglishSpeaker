#!/usr/bin/python3

# required modules
from gtts import gTTS
from playsound import playsound
from random import choice,choices
from os import system,remove,getcwd
from termcolor import colored,cprint
import platform

# terminal cleaner, it checks if OS is WINDOWS or NOT WINDOWS and clean the terminal with right command
def cleaner():

        if platform.system() == "Windows":
                system("cls")
        else:
                system("clear")

# about authour
def aboutme():

        print("\n","\t"*3,end=""),cprint("===>  ","white",attrs=["bold"],end=""),cprint("Please Turn Up The Volume","grey",attrs=["bold","blink"],end=""),cprint("   <===","white",attrs=["bold"],end="") ,print("\t"*4,end=""),cprint("####  ","white",attrs=["bold"],end=""),cprint("By  : Abd Almoen Arafa (0.1Arafa)","yellow",attrs=["bold"],end=""),cprint("  ####","white",attrs=["bold"]),print("\t"*11,end=""),cprint("####  ","white",attrs=["bold"],end=""),cprint("Age : 15			      ","yellow",attrs=["bold"],end=""),cprint("   ####","white",attrs=["bold"])

# MainScriptIdea
def mainscript():

        cprint("\n[ ","white",attrs=["bold"],end="")
        cprint("*","green",attrs=["bold"],end="")
        cprint(" ]","white",attrs=["bold"],end=" ")
        cprint("Difficulty Level ","magenta",attrs=["bold"],end="")
        cprint("( ","white",attrs=["bold"],end="")
        cprint("EASY","magenta","on_white",attrs=["bold","blink"],end="")
        cprint(" , ","white",attrs=["bold"],end="")
        cprint("MEDIUM","magenta","on_white",attrs=["bold","blink"],end="")
        cprint(" , ","white",attrs=["bold"],end="")
        cprint("HARD","magenta","on_white",attrs=["bold","blink"],end="")
        cprint(" , ","white",attrs=["bold"],end="")
        cprint("VERY HARD","magenta","on_white",attrs=["bold","blink"],end="")
        cprint("/","white",attrs=["bold"],end="")
        cprint("EXPERT","magenta","on_white",attrs=["bold","blink"],end="")
        cprint(" , ","white",attrs=["bold"],end="")
        cprint("LEGEND","magenta","on_white",attrs=["bold","blink"],end="")
        cprint(" )","white",attrs=["bold"],end="")
        levelask=input(colored(": ","magenta",attrs=["bold"])).strip()
        count,Count,counT=1,2,0
        while Count > count:
                text="cat.dog.sun.moon.star.tree.car.book.pen.hat.shoe.cup.bed.ball.fish.apple.bird.cake.chair.door.frog.grass.house.kite.leaf.milk.mouse.pencil.rain.road.ship.soap.spoon.table.train.water.window.boat.bread.cloud.corn.dress.flower.hand.horse.ice.lamp.map.nest.snow.bike.baby.egg.farm.game.girl.hill.jam.king.lamb.lion.man.owl.park.queen.ring.sock.truck.van.wave.yard.zebra.ant.bear.cow.duck.ear.fire.goat.hat.ink.jar.key.leg.moon.nose.orange.pig.quilt.rock.sun.top.umbrella.vase.wolf.ax.box.cake.dish.eye.frog.gum.hen.iron.jug.kite.log.mop.net.ox.pan.rug.sock.tent.urn.well.yarn.zip.apple.ball.drum.elf.fan.gum.ice.jam.kite.leaf.mop.owl.pie.quill.rat.sun.top.urn.vase.web.x-ray.yak.zoo.bear.cat.dog.egg.fox.goat.hen.ink.jar.key.log.mop.net.ox.pan.rug.sock.tent.urn.well.yarn.zip.april.bat.cup.drum.elf.fan.gum.hen.ink.jar.kit.log.mat.nut.owl.pie.quill.rat.sun.top.urn.vase.web.x-ray.yak.zoo.april.box.car.dog.elf.fan.gum.hen.ink.jug.key.log.mat.nut.owl.pie.quill.rat.sun.top.urn.vase.web.yak.zoo.name.will you hold on.even if.door.window.roof.stairs.carpet.bed.bad.both.perfume.look at me.battle.war.when you light the candle.got the music in you baby tell me why.motion.picture.it's leading me on.soundtrack.opera house.blessed.curse.drown.throne.the final episode.scream.aim.fire.true friends.bad idea.dead girl in the pool.reach out.fit in with.listen to me.loyal.honest.values first.pray.smile.london.apocalypse.monsters.eagle.master.royal.jenny.henry.lucas.t-shirt.captain black.ungrateful.don't lean on me.disposable.can i call you tonight.dumb.flash.nothing's gonna hurt you baby.pistol.don't hurt me.seventeen.upside down.dead but pretty.fight this.lips.apartment.depression.stupid.unanswered.reflection.build.sugar.salt.salty.reasons to.pretty.shape.tell me about you.late night.winter.shine a light.trapped.until we leave the ground.crying in your sweater.afraid.lonely.sunflower.youth.mountain.covered.i know you so well.my girl.your girl.our girl.you make it worse.bleeding out.cinnamon.instrumental.voices.firefighter.cannonball.say goodbye.empty.puppets.snow.scissor.cycle.rats.city lights.will you still love me.negative.before i forget.moonlight.sicko mode.crime.promise me.last of us.worn out.the other side.teardrops.go to hell.for heaven's sake.alison.control.issues.money.addicted.left behind.the devil in i.hive mind.you broke my heart again.heart of glass.squeeze.mercury.black blood.born to die.where do lovers go.the city holds my heart.placeholder.jealous.space.call me.miss you.sometimes it ends.in the end.affection.sunsetz.dreaming of you.starry eyes.what can i say.attention.moral of the story.fade into you.almost.shadow.theme.diary.fly me to the moon.sport.godzilla.parasite.god knows i tried.high by the beach.sniff.smell.honeymoon.send me an angel.after dark.sweater weather.free.highway.inside out.sing.natural.thunder.a dark knight.touch my back and i'll touch yours.sunlight on your skin.ghostly kisses.backwards.punch.shine.sam.medicine.some say.somewhat interesting.the brightside.save that shit.gym class.don't be weak.nasty names.ring.line without a hook.let go.cry alone.airplanes.white tee.change your mind.say yes to heaven.beat it.smooth criminal.sorry for me.don't be sad.come a little closer.cruel world.regret.just in case.watch.me and the birds.switch up.don't be mad.violent dreams.florida.lost cause.new flesh.out of my league.sweet dreams.white noise.bubblegum.make me famous.the blonde.die hard.tell my mother i'm sorry.move on.be strong.middle east.up up and away.end my life.crazy.wait a minute.crush on you.i love you baby.weird.catch.swim.faceless.fed up.the perfect.radio.summertime sadness.a little death.i just wanna be your sweetheart.you said.too close.zombie.i can't find anyone.message man.give me your heart.kiss your hand.to infinity.let me get what i want.electric feel.jungle.in your arms.take me home.country roads.christmas kids.my time is here.and i'll make it clear.spit in your face.one last time.there is a light that never goes out.crashes into us.to die by your side.is such a heavenly way to die.oh i love you my dear.but i'm gone.i might come back.i could stop time.sleep on the floor.open your eyes.thank you.my own summer.wicked game.we fell in love in october.mary on a cross.thank you.be quiet and drive.live forever.best person you know.haunted.all girls are the same.look up.want me.i was all over her.bones.freak show.fall back.first love.late spring.let it happen.save me.faster.harder.right here.runaway.hide your kids.when it happen.when the devil speaks.south west.convert.psychosocial.american psycho.chinatown.forrest gump.taxi driver.baby blue movie.stop waiting.placement.come right back.i've been waiting for you.in trouble.when you know you know.and share my body.and share my mind.with you.no.yes.sure.happy.mode.gold.silver.paste.past.copy.move.movies.moon.can i get you the moon.was come on for you.car.window.metal.wood.turtle.lion.eagle.jaguar.shark.snake.block.tent.maybe.error.present.after.both.before.put.castle.bad guy.age.how much.it's a hard work.you always be my day one.don't really wanna die i just wanna feel alive.how long.how many.steam.stream.live.govern.about.long.this.around.play.by.these.those.this.at.now.own.give.look at me.life.nano.science.exit.quit.black screen.blue screen.white screen.park.part.party.pretty.pretty face.so much fun.each.approach.increase.ability.benefits.fit girl.fat girl.fit boy.fat boy.point.enter.star.stick.toxic.nine.has been.society.fuck society.thankful.apple.orange.i got you.did you get it.say hello for me.where are you from.how old are you.what's your name.do you like sciences.do you like the music.rockbye baby.don't cry please.just like this.it was the end.best movies.shorts.shoes.the end.you're my day one.come and smell this flower.i'll eat this.are you here.is she there.hello,how are you today.are you okay.don't look at me like this.it's a bad feelings.it's your cat or what.i'm going to my home.wide pool.world wide.nice tree.around the world.all over the world.come here boy.come here girl.what's your favourite color.peace out.rest in peace.it's a nice car.purple car.green car.hot wheels.turkey.england.syria.egypt.algeria.america.colombia.germany.africa.middle east.canada.moroco.lebanon.iraq.middle east servers.europe.open this file.heaven.darkest day.give me the loop.high performance.large icon.low battery.don't run away.look at me.locked phone.hard battle.nice game.thug life.a lot of money.there is a cd there.the floor is too long.what is your language.i like this wall.let's make some noise.beautiful table.she's the tallest woman.are you there.bodybuilding is dangerous when playing fault.stop please.read this.turn off this computer.turn on the ps4.her hair is too long.she's a blonde woman.blue eyes.let's play together on this phone.don't run while the weather is stormy.it was a hard day.just read this.study for your test.you just want attention.trust me.can i get you the moon.sunshine.machine.application.exciting challenge.let's go.i don't know.i know it.i swear to god.animal.generator.purple.what the fuck.may i help you.can i see you.click here.this is for test.how are you.is that you.how old are you.ok thank you.come on over in my direction.isn't lovely all alone.baby don't leave me.begginer.are you a human.i think he's right.ok peace.see you later.i can't hold on.i'm waiting for you.hang on.please don't break my heart.he's a boy.boy.she's a girl.girl.maths.numbers.are you alone.bullshit.you're right.fault.alive.can you hate me.i love you.my mom.i love that.sky.the sky is high.key.robot.dark.high building.weight.password.email.raise of nations.general.computer.are you a child.children.television.one hundred.thousands of people.lover.i can't wait for it.control.touchpad.character.mother.father.son.family.daughter.cousin.grandmother.grandfather.nice body.cute one.he's a tall man.i like him.i like her.is she need me.need is need.fire.sing with me.what is the best song for you.singer.female.male.make.made.cooking.my mom's cooking a nice food.cheese.meeting.mate.university.school.primary school.dog.cat.turtle.airplane.telephone.house.uniform.notebook.book.horor.pencil.afraid.changes.i won't let you go.let me love you.kill the monster.don't play this game again.do you wanna come with me.yes write this.no man i don't like it.under the sea.brown skin.white leather.let's drink this.are you ready.refresh.guide book.restaurant.sort by.view.quickly please.nice clothes.hot food.spicy food.deep sea.adult man.adult woman.oldman.oldwomen.group of youngs.baby you can hold me.bettery.charger.telephone.light.motion.easly.fast.create.chat.zoom.zoo.input.output.display.desktop.launcher.join us.call me later.as tall as.meeting.angry.after.again.also.against.area.baby.away.bad.bag.boy.agency.although.above.about.add.address.affect.administrator.hungry.east.west.south.north.different.island.fairly.juice.kiss.knife.rain.bury.damage.umbrella.violent.wire.worth.worst.ugly.teach.learn.safe.safely.rainbow.library.cartoon.network.awesome.huge.healthy.handsome.gentle.delicious.energy.famous.family.farm.from.camera.careful.carefully.attractive.bigger.fitter.but".split(".")
                List=[1,2,3,4,5,6,7,8,9,10,15]
                if levelask.lower() == "easy":
                        main_text=choice(text)
                elif levelask.lower() in ("medium","hard","very hard","expert","legend"):
                        if levelask.lower() == "medium":
                                many=choice(List[1:3])
                        elif levelask.lower() == "hard":
                                many=choice(List[3:6])
                        elif levelask.lower() in ("very hard","expert"):
                                many=choice(List[6:10])
                        elif levelask.lower() == "legend":
                                many=List[10]
                        answer=choices(text,k= many)
                        main_text= " ".join(answer)
                elif levelask.lower() in ("exit","quit"):
                        print("\n")
                        quit()
                else:
                        cleaner()
                        aboutme()
                        mainscript()
                print("\t"*8,end="")
                cprint("Your Points: ","blue",attrs=["bold"],end="")
                cprint(counT,"green",attrs=["bold"])
                cprint("[ ","grey",attrs=["bold"],end="")
                cprint(count,"green",attrs=["bold"],end="")
                cprint(" ]","grey",attrs=["bold"],end=" ")
                ask=input(colored("Are you ready? ( Y , N , RESTART ): ","blue",attrs=["bold"])).strip()
                if ask.lower() in ("n","no","exit","quit"):
                        print("\n")
                        quit()
                elif ask.lower() in ("restart","replay","play again"):
                        cleaner()
                        aboutme()
                        mainscript()
                else:

                        def connect():
               
                                try:
                                        speaker=gTTS(text=main_text, lang="en") # choosing the text and the language
                                        speaker.save("audio.mp3") # creating file that it will be play
                                except KeyboardInterrupt:
                                        cprint("\n[!] Stopped by the user.","yellow","on_red",attrs=["bold"])
                                        exit()
                                except: # reconnecting when network error
                                        cprint("[-] ERROR: Network error, ","red",attrs=["bold"],end="")
                                        cprint("trying to connect...","red",attrs=["reverse","blink"])
                                        connect()
               
                        def play():
               
                                try:
                                        playsound(f"{getcwd()}\\audio.mp3") # SoundPlaying
                                except KeyboardInterrupt:
                                        cprint("\n[!] Stopped by the user.","yellow","on_red",attrs=["bold"])
                                        exit()
                                except:
                                        play()
                
                        connect()
                        play()
                        remove("audio.mp3") # removing the file
                        cprint("  ?   ","white",attrs=["bold"],end="")
                        ask=input(colored("Your answer: ","blue",attrs=["bold"])).strip()
                        if ask.lower() == main_text:
                                cprint("True ;)","cyan",attrs=["bold"],end="\n")
                                counT+=1
                        else:
                                cprint("False :(\nThe right answer:","red",attrs=["bold"],end=" ")
                                cprint(main_text,"yellow","on_magenta",attrs=["bold"])
                                counT-=1
                        count+=1
                        Count+=1

if __name__ == "__main__":

        try:
                cleaner()
                aboutme()
                mainscript()
        except KeyboardInterrupt:
                cprint("\n[!] Stopped by the user.","yellow","on_red",attrs=["bold"])
                exit()
                
#By : Abd Almoen Arafa (0.1Arafa)
#Age : 15
