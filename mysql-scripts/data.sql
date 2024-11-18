USE FabiaNatura;

-- Inserción de datos en la tabla Proveedores
INSERT INTO Proveedores (ruc, nombre) VALUES
('20101796532', 'NATURA COSMETICOS S.A.'),
('20100078792', 'PRODUCTOS AVON S.A.'),
('20517667502', 'ESIKA COSMETICS PERU S.A.C.');

-- Inserción de datos en la tabla Telefonos_Proveedores
INSERT INTO Telefonos_Proveedores (ruc, telefono) VALUES
('20101796532', '440-1362'),
('20100078792', '317-2866'),
('20517667502', '0801-1-3030');

-- Inserción de datos en la tabla Categorias
INSERT INTO Categorias (nombre, descripcion) VALUES
('Maquillaje', 'Productos diseñados para embellecer y resaltar los rasgos del rostro, ofreciendo opciones para diferentes tonos de piel, estilos y ocasiones.'),
('Fragancias', 'Perfumes y colonias para hombres y mujeres, diseñados para reflejar la personalidad y estilo de quien los usa. Estas fragancias suelen estar desarrolladas con notas florales, cítricas, amaderadas o dulces.'),
('Cuidado de la piel', 'Productos especializados para mantener una piel saludable, hidratada y protegida, adaptados a diferentes tipos de piel (seca, grasa, mixta o sensible).'),
('Cuidado del cabello', 'Productos diseñados para limpiar, hidratar, reparar y estilizar el cabello, con opciones para diferentes necesidades capilares.'),
('Bienestar', 'Productos orientados al autocuidado integral, promoviendo la relajación y el equilibrio.');

-- Inserción de Productos de Natura:
INSERT INTO Productos (cod_categoria, ruc, nombre, linea, descripcion, precio_compra, precio_venta, stock, estado) VALUES 
(2, '20101796532', 'Essencial masculino', 'Essencial', 'Amaderado intenso.', 104.5, 125.4, 1, 'disponible'),
(2, '20101796532', 'Kaiak clásico masculino', 'Kaiak', 'Aromático herbal. leve, notas acuosas, albahaca, bergamota.', 64.5, 77.4, 12, 'disponible'),
(2, '20101796532', 'Kriska Shock', 'Kriska', 'Desodorante corporal en spray 100 ml', 93.0, 111.6, 2, 'disponible'),
(2, '20101796532', 'Kaiak urbe masculino', 'Kaiak', 'Aromático herbal. moderado, notas acuosas, sándalo, ámbar.', 64.5, 77.4, 3, 'disponible'),
(2, '20101796532', 'Humor femenino rosa', 'Humor', 'Una fragancia irreverente, enriquecida con ingredientes naturales inéditos brasileños.', 63.0, 75.6, 7, 'disponible'),
(2, '20101796532', 'Ekos frescor pitanga', 'Ekos', 'Notas de pitanga negra conviven con flores de colores y ganan un toque de notas amaderadas.', 61.8, 74.16, 1, 'disponible'),
(2, '20101796532', 'Colonia formas en las nubes', 'Nature', 'Una colonia ideal para acompañar momentos de pura diversión y destapar tu lado creativo.', 64.0, 76.8, 1, 'disponible'),
(2, '20101796532', 'Colonia jugando en los árboles', 'Nature', 'Una invitación a sentir la divertida sensación de jugar en la naturaleza por medio de una fragancia cítrica.', 64.0, 76.8, 6, 'disponible'),
(1, '20101796532', 'Labial cremoso multimix', 'Faces', 'Más capas, más color con efecto cremoso, bye bye a los labios resecos, producto vegano.', 27.0, 32.4, 11, 'disponible'),
(1, '20101796532', 'Esmalte 3D gel negro', 'Una', 'Cobertura uniforme. Favorece la nutrición de las uñas. Larga duración y brillo extraordinario.', 24.0, 28.8, 1, 'disponible'),
(1, '20101796532', 'Esmalte 3D gel marrón', 'Una', 'Cobertura uniforme. Favorece la nutrición de las uñas. Larga duración y brillo extraordinario.', 24.0, 28.8, 1, 'disponible'),
(1, '20101796532', 'Esmalte 3D gel rojo', 'Una', 'Cobertura uniforme. Favorece la nutrición de las uñas. Larga duración y brillo extraordinario.', 24.0, 28.8, 3, 'disponible'),
(1, '20101796532', 'Esmalte 3D gel celeste', 'Una', 'Cobertura uniforme. Favorece la nutrición de las uñas. Larga duración y brillo extraordinario.', 24.0, 28.8, 11, 'disponible'),
(1, '20101796532', 'Maxxi palette de sombras nude', 'Una', 'Alta cobertura. Amplia variedad de tonalidades, desde mate hasta perlado. Para looks naturales hasta los más elaborados.', 102.0, 122.4, 8, 'disponible'),
(3, '20101796532', ' Sérum intensivo multiaclarador', 'Chronos', 'Sérum que ayuda a reducir manchas y unificar el tono de la piel, proporcionando luminosidad y mejorando la textura.', 121.0, 145.2, 5, 'disponible'),
(3, '20101796532', 'Acqua biohidratante', 'Chronos', 'Hidratante ligero que proporciona una hidratación profunda y duradera, ideal para todo tipo de piel.', 141.0, 169.2, 11, 'disponible'),
(3, '20101796532', 'Gel crema antiseñales noche 30 ', 'Chronos', 'Crema nocturna que combate los primeros signos de envejecimiento, mejorando la firmeza y elasticidad de la piel.', 141.0, 169.2, 7, 'disponible'),
(3, '20101796532', 'Protector hidratante antioleosidad FPS 30', 'Chronos', 'Protector solar facial que controla la oleosidad y brinda protección contra los rayos UV, ideal para pieles mixtas a grasas.', 80.0, 96.0, 4, 'disponible'),
(3, '20101796532', 'Pulpa hidratante corporal castaña', 'Chronos', 'Crema corporal que nutre e hidrata profundamente la piel, dejándola suave y perfumada.', 59.0, 70.8, 1, 'disponible'),
(3, '20101796532', 'Crema hidratante corporal frutas rojas', 'Tododia', 'Hidratante corporal de rápida absorción que deja la piel suave y con una fragancia delicada.', 54.3, 65.16, 8, 'disponible'),
(3, '20101796532', 'Hidratante facial aclarador piel seca', 'Faces', 'Hidratante facial que unifica el tono de la piel y proporciona hidratación intensa, especialmente formulado para piel seca.', 33.0, 39.6, 13, 'disponible'),
(3, '20101796532', 'Máscara de arcilla purificante', 'Chronos', 'Mascarilla facial que limpia profundamente, removiendo impurezas y controlando el exceso de oleosidad.', 65.0, 78.0, 8, 'disponible'),
(3, '20101796532', 'Loción protectora facial FPS 50', 'Fotoequilíbrio', 'Protector solar facial para piel normal a seca, que previene el envejecimiento prematuro y es resistente al agua y al sudor hasta por 3 horas.', 80.0, 96.0, 13, 'disponible'),
(3, '20101796532', 'Gel crema protector facial FPS 50', 'Fotoequilíbrio', 'Protector solar facial para piel mixta a oleosa, con textura ligera, rápida absorción y toque seco.', 80.0, 96.0, 13, 'disponible'),
(4, '20101796532', 'Shampoo matizador brillo y protección del color', 'Lumina', 'Realza el brillo y protege el color del cabello teñido, manteniendo su vitalidad por más tiempo.', 34.0, 40.8, 10, 'disponible'),
(4, '20101796532', 'Shampoo estimulante anticaída y crecimiento', 'Lumina', 'Fortalece el cabello y estimula su crecimiento, reduciendo la caída capilar.', 34.0, 40.8, 2, 'disponible'),
(4, '20101796532', 'Shampoo reestructurante limpieza y reparación', 'Lumina', 'Limpia profundamente mientras repara la estructura del cabello dañado, dejándolo más resistente y saludable.', 34.0, 40.8, 2, 'disponible'),
(4, '20101796532', 'Shampoo revitalizante brillo y protección del color', 'Lumina', 'Revitaliza el cabello teñido, aportando brillo y protegiendo el color de los daños diarios.', 34.0, 40.8, 7, 'disponible'),
(4, '20101796532', 'Shampoo nutritivo reparación y nutrición', 'Lumina', 'Proporciona una nutrición profunda, reparando el cabello seco y dejándolo suave y manejable.', 40.0, 48.0, 4, 'disponible'),
(4, '20101796532', 'Crema para peinar modeladora', 'Lumina', 'Define e hidrata el cabello, facilitando el peinado y controlando el frizz.', 34.0, 40.8, 7, 'disponible'),
(4, '20101796532', 'Spray humidificador reactivador de rizos', 'Lumina', 'Reactiva y define los rizos, aportando hidratación y control del frizz durante el día.', 34.0, 40.8, 4, 'disponible'),
(4, '20101796532', 'Óleo leve reparador', 'Lumina', 'Aceite ligero que repara las puntas abiertas y proporciona brillo sin dejar el cabello pesado.', 34.0, 40.8, 8, 'disponible'),
(5, '20101796532', 'Aceite trifásico de maracuyá', 'Ekos', 'Aceite corporal con tres fases que hidratan y perfuman la piel, proporcionando frescura y relajación gracias a las propiedades calmantes del maracuyá.', 62.0, 74.4, 12, 'disponible'),
(5, '20101796532', 'Jabón exfoliante', 'Ekos', 'Jabón en barra con partículas exfoliantes naturales que eliminan células muertas, revitalizan la piel y aportan una fragancia energizante de acaí.', 28.0, 33.6, 6, 'disponible'),
(5, '20101796532', 'Pulpa hidratante para manos de castaña', 'Ekos', 'Crema de manos enriquecida con aceite de castaña, que hidrata y fortalece la piel, dejando las manos suaves y con una agradable fragancia.', 30.0, 36.0, 13, 'disponible'),
(5, '20101796532', 'Aceite de masaje andiroba', 'Ekos', 'Aceite corporal formulado con aceite de andiroba, conocido por sus propiedades antiinflamatorias y relajantes, ideal para masajes que alivian tensiones y promueven el bienestar.', 65.0, 78.0, 4, 'disponible');

-- Inserción de Productos de Avon:
INSERT INTO Productos (cod_categoria, ruc, nombre, linea, descripcion, precio_compra, precio_venta, stock, estado) VALUES 
(1, '20100078792', 'Labial ultramate FPS 15 marvelous mocha', 'True color', 'Labial de acabado ultramate que proporciona un color intenso y duradero, enriquecido con FPS 15 para proteger los labios.', 21.9, 26.2, 1, 'disponible'),
(1, '20100078792', 'Brillo para labios fresita color trend', 'Color trend', 'Brillo labial con aroma a fresa que aporta un toque de color y brillo, ideal para un look fresco y juvenil.', 16.9, 20.2, 3, 'disponible'),
(1, '20100078792', 'Base mate en barra FPS 20 medio matte real', 'Matte real', 'Base de maquillaje en formato barra con acabado mate, ofrece cobertura media y protección solar FPS 20.', 20.9, 25.08, 3, 'disponible'),
(1, '20100078792', 'Spray preparador y fijador de maquillaje', 'True color', 'Spray multifuncional que prepara la piel antes del maquillaje y fija el look para una mayor duración.', 20.9, 25.08, 8, 'disponible'),
(1, '20100078792', 'Máscara para pestañas ultra volume a prueba de agua', 'True color', 'Máscara que aporta volumen extremo a las pestañas, resistente al agua para una duración prolongada.', 20.9, 25.08, 7, 'disponible'),
(1, '20100078792', 'Delineador líquido para ojos azul metálico color trend', 'Color trend', 'Polvo compacto que ayuda a controlar el brillo y unificar el tono de la piel, incluye espejo para retoques.', 21.9, 26.2, 7, 'disponible'),
(1, '20100078792', 'Corrector líquido neutral fair power stay', 'Power stay', 'Corrector líquido de larga duración que cubre imperfecciones y ojeras, tono Neutral Fair.', 25.9, 31.08, 11, 'disponible'),
(1, '20100078792', 'Labial hydramatic matte fawn', 'Hydramatic', 'Labial mate con centro hidratante que proporciona color intenso y confort durante todo el día.', 24.9, 29.88, 10, 'disponible'),
(2, '20100078792', 'Colonia para niños avengers', 'Fragancias infantiles', 'Colonia inspirada en los personajes de Avengers, indicada para niños a partir de los 3 años. Dermatológicamente comprobada.', 19.9, 23.88, 3, 'disponible'),
(2, '20100078792', 'Colonia para niños SpiderMan de marvel', 'Fragancias infantiles', 'Colonia con temática de SpiderMan, diseñada para niños mayores de 3 años. Dermatológicamente probada.', 20.9, 25.08, 12, 'disponible'),
(2, '20100078792', 'Black suede hot', 'Black suede', 'Fragancia masculina con notas orientales y amaderadas, ideal para ocasiones especiales.', 47.9, 57.48, 12, 'disponible'),
(2, '20100078792', 'Musk marine', 'Musk', 'Colonia refrescante con aroma herbal y aromático, perfecta para el uso diario.', 20.9, 25.08, 4, 'disponible'),
(2, '20100078792', 'Soft musk vainilla', 'Soft musk', 'Perfume femenino con notas suaves de vainilla, brindando un aroma dulce y delicado.', 34.9, 41.8, 6, 'disponible'),
(2, '20100078792', 'Secret fantasy', 'Secret fantasy', 'Fragancia con aroma floral y frutal, ideal para mujeres jóvenes que buscan un toque de frescura.', 25.4, 30.4, 10, 'disponible'),
(3, '20100078792', 'Anew hydra fusion gel-crema', 'Anew hydra fusion', 'Gel-crema hidratante que proporciona hidratación profunda y mejora la elasticidad de la piel seca.', 89.9, 107.8, 13, 'disponible'),
(3, '20100078792', 'Clearskin professional crema facial matificante', 'Clearskin professional', 'Crema ligera que controla el exceso de grasa y deja un acabado mate en pieles grasas.', 29.9, 35.8, 11, 'disponible'),
(3, '20100078792', 'Nutraeffects balance gel-crema', 'Nutraeffects balance', 'Gel-crema que hidrata las zonas secas y controla el brillo en pieles mixtas.', 39.9, 47.879999999999995, 7, 'disponible'),
(3, '20100078792', 'Anew sensitive crema calmante', 'Anew sensitive', 'Crema formulada para calmar y reducir la irritación en pieles sensibles, fortaleciendo su barrera protectora.', 99.9, 119.8, 3, 'disponible'),
(3, '20100078792', 'Nutraeffects crema hidratante con SPF 15', 'Nutraeffects', 'Crema hidratante que proporciona nutrición intensa y protección solar para pieles secas.', 49.9, 59.8, 2, 'disponible'),
(3, '20100078792', 'Nutraeffects balance tónico facial', 'Nutraeffects', 'Tónico facial que equilibra la piel mixta, reduce el exceso de grasa y tonifica las áreas secas.', 24.9, 29.88, 10, 'disponible'),
(3, '20100078792', 'Nutraeffects active seed crema revitalizante noche', 'Nutraeffects', 'Crema de noche que nutre y regenera la piel seca mientras duermes.', 55.9, 67.08, 3, 'disponible'),
(4, '20100078792', 'Advance techniques shampoo nutrición completa', 'Advance techniques', 'Shampoo formulado con aceite de argán y coco que limpia suavemente mientras nutre profundamente el cabello seco y dañado, dejándolo suave y brillante.', 31.9, 38.28, 11, 'disponible'),
(4, '20100078792', 'Advance techniques acondicionador reparación intensa', 'Advance techniques', 'Acondicionador que repara y fortalece el cabello dañado, reduciendo la rotura y las puntas abiertas, para un cabello más saludable y manejable.', 16.9, 20.2, 1, 'disponible'),
(4, '20100078792', 'Advance techniques mascarilla hidratante', 'Advance techniques', 'Mascarilla intensiva que proporciona una hidratación profunda, restaurando la suavidad y el brillo del cabello seco y opaco.', 16.9, 20.2, 7, 'disponible'),
(4, '20100078792', 'Advance techniques sérum anti-frizz', 'Advance techniques', 'Sérum ligero que controla el frizz y aporta un brillo instantáneo, dejando el cabello suave y sedoso sin sensación grasosa.', 24.9, 29.88, 10, 'disponible'),
(4, '20100078792', 'Advance techniques spray protector térmico', 'Advance techniques', 'Spray que protege el cabello del daño causado por herramientas de calor, como planchas y secadores, manteniendo la hidratación y evitando la rotura.', 29.9, 35.8, 1, 'disponible');

-- Inserción de Productos de Unique:
INSERT INTO Productos (cod_categoria, ruc, nombre, linea, descripcion, precio_compra, precio_venta, stock, estado) VALUES 
(1, '20517667502', 'Delineador lápiz para labios', 'Ésika pro', 'Lápiz delineador de labios con trazo suave y alta pigmentación, ideal para definir y dar volumen a los labios.', 30.0, 36.0, 5, 'disponible'),
(1, '20517667502', 'Labial colorfix 24h', 'ColorFix', 'Labial de larga duración que ofrece color intenso y acabado mate, manteniéndose intacto hasta por 24 horas.', 47.0, 56.4, 12, 'disponible'),
(1, '20517667502', 'Delineador líquido punta plumón eye pro', 'Eye pro', 'Delineador líquido con punta tipo plumón que permite trazos precisos y definidos, ideal para delinear los ojos con facilidad.', 48.0, 57.6, 3, 'disponible'),
(1, '20517667502', 'Labial mate color addiction', 'Color  addiction', 'Labial de acabado mate que proporciona un color vibrante y duradero, con una textura suave y cremosa.', 40.0, 48.0, 10, 'disponible'),
(1, '20517667502', 'Máscara mega full size a prueba de agua', 'Mega full size', 'Máscara de pestañas resistente al agua que aporta volumen extremo y definición, manteniendo las pestañas impecables durante todo el día.', 57.0, 68.4, 2, 'disponible'),
(2, '20517667502', 'Vibranza', 'Vibranza', 'Perfume de mujer oriental dulce, de la colección #1 en ventas de Ésika, con irresistibles notas de orquídea de vainilla y flor de café, para la mujer sensual, segura y que sabe lo que quiere.', 153.0, 183.6, 5, 'disponible'),
(2, '20517667502', 'Dream', 'Dream', 'Nuevo perfume de mujer floral frutal con brillantes notas de pera francesa, esencia de flor de magnolia y madera de cedro, para la mujer audaz, vibrante y llena de energía.', 115.0, 138.0, 11, 'disponible'),
(2, '20517667502', 'Magnat select', 'Magnat', 'Perfume de hombre con notas amaderadas y especiadas, ideal para el hombre elegante y sofisticado.', 180.0, 216.0, 5, 'disponible'),
(2, '20517667502', 'Kromo black', 'Kromo', 'Perfume de hombre con notas frescas y cítricas, perfecto para el hombre dinámico y moderno.', 180.0, 216.0, 10, 'disponible'),
(2, '20517667502', 'Pulso absolute', 'Pulso', 'Perfume de hombre edición limitada con notas intensas y masculinas, diseñado para el hombre seguro de sí mismo.', 174.0, 208.8, 12, 'disponible'),
(3, '20517667502', 'Protector solar facial antiedad FPS 100 triple acción max', 'Ésika skincare', 'Protector solar facial en loción con complejo de vitamina B5 y vitamina E que hidrata y brinda acción antioxidante. Su exclusiva tecnología combina poderosos filtros solares que protegen de los 4 tipos de radiación que causan envejecimiento y manchas. Capacidad: 40 g.', 55.8, 66.96, 12, 'disponible'),
(3, '20517667502', 'Protector solar para rostro y cuerpo perfect block', 'Ésika skincare', 'Protector solar para rostro y cuerpo resistente al agua y sudor. Dermatológicamente probado. Capacidad: 80 ml.', 81.0, 97.2, 10, 'disponible'),
(3, '20517667502', 'Protector solar para rostro perfect block', 'Ésika skincare', 'Multiprotector solar para rostro en loción con FPS 50, UVA, UVB, luz visible y azul. Alta protección con acabado mate compatible con tu maquillaje. Capacidad: 50 ml.', 66.6, 79.9, 2, 'disponible'),
(3, '20517667502', 'Sérum facial revitalizante con vitamina C', 'Ésika skincare', 'Sérum facial con alta concentración de vitamina C que ayuda a iluminar y revitalizar la piel, reduciendo signos de fatiga y aportando un aspecto radiante.', 120.0, 144.0, 3, 'disponible'),
(3, '20517667502', 'Sérum facial antimanchas con niacinamida', 'Ésika skincare', 'Sérum facial que combina niacinamida y otros activos para reducir la apariencia de manchas y unificar el tono de la piel, brindando luminosidad y suavidad.', 125.0, 150.0, 8, 'disponible'),
(4, '20517667502', 'Shampoo 2 en 1 tutti frutti mini chics', 'Mini chics', 'Shampoo y acondicionador en un solo producto, con fragancia de tutti frutti, diseñado para limpiar y suavizar el cabello de los niños.', 43.2, 51.84, 6, 'disponible'),
(4, '20517667502', 'Desenredante mini chics', 'Mini chics', 'Spray desenredante que facilita el peinado del cabello infantil, dejando un aroma agradable y evitando tirones.', 43.2, 51.84, 5, 'disponible'),
(4, '20517667502', 'Shampoo 3 en 1 alviento fortalecimiento y prevención caída', 'Alviento', 'Shampoo para hombres con acción fortalecedora que limpia profundamente, previene la caída y deja el cabello con un aspecto saludable.', 59.9, 71.88, 7, 'disponible'),
(4, '20517667502', 'Gel fijador para hombres alviento efecto natural', 'Alviento', 'Gel fijador con efecto natural que estiliza el cabello sin dejar residuos, ideal para looks casuales o formales.', 49.9, 59.8, 3, 'disponible'),
(4, '20517667502', 'Shampoo hidratante balance pro mujeres', 'Balance pro', 'Shampoo diseñado para hidratar profundamente el cabello seco o maltratado, dejando un acabado sedoso.', 65.9, 79.0, 12, 'disponible'),
(4, '20517667502', 'Mascarilla capilar nutritiva balance pro', 'Balance pro', 'Mascarilla nutritiva para cabello seco, que restaura la vitalidad y suavidad desde la raíz hasta las puntas.', 75.9, 91.0, 7, 'disponible'),
(5, '20517667502', 'Emotions calm eau de parfum', 'Emotions calm', 'Fragancia con notas de lavanda y aceite de geranio 100% naturales, diseñada para brindar una sensación de calma y tranquilidad.', 92.0, 110.4, 10, 'disponible'),
(5, '20517667502', 'Emotions calm crema hidratante para manos', 'Emotions calm', 'Crema de rápida absorción con manteca de karité que nutre e hidrata las manos, dejando un aroma relajante.', 43.0, 51.6, 5, 'disponible'),
(5, '20517667502', 'Emotions calm crema corporal ultra hidratante', 'Emotions calm', 'Crema corporal con textura tipo manteca que brinda hidratación y nutrición hasta por 48 horas, ideal para una experiencia de relajación.', 58.0, 69.6, 5, 'disponible'),
(5, '20517667502', 'Loción hidratante agú con aroma relajante', 'Agú', 'Loción hidratante con aroma a lavanda y jazmín, formulada con extractos 100% de origen natural, perfecta para promover el equilibrio emocional.', 45.0, 54.0, 10, 'disponible'),
(5, '20517667502', 'Aceite relajante para masaje', 'Emotions relax', 'Aceite de masaje con extractos naturales que relajan los músculos y promueven un estado de bienestar.', 49.9, 59.8, 13, 'disponible'),
(5, '20517667502', 'Gel exfoliante corporal', 'Calming vibes', 'Gel exfoliante con partículas naturales que remueven las células muertas mientras relajan los sentidos con su aroma suave.', 42.0, 50.4, 12, 'disponible'),
(5, '20517667502', 'Spray aromático para almohadas y ambiente', 'Agú', 'Spray formulado con aceites esenciales que ayuda a crear un ambiente relajante, ideal para promover un descanso profundo.', 50.0, 60.0, 1, 'disponible');