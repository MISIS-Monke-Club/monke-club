import { useParams } from "react-router-dom"
import { useQuery } from "@tanstack/react-query"
import classes from "./detailed-request-page.module.scss"
import { api } from "@features/request/by-id"
import { FullRequestModel } from "@features/request/by-id"
import { Icon } from "@shared/ui/icon"
import { Tag } from "@shared/ui/tag"

export function RequestDetail() {
    const { slug } = useParams<{ slug: string }>()

    const { data, isLoading, isError } = useQuery<FullRequestModel>(
        api.getRequestBySlug(slug!)
    )

    if (isLoading) return <div>Загрузка...</div>
    if (isError) return <div>Ошибка при загрузке заявки</div>
    if (!data) return <div>Заявка не найдена</div>

    return (
        <>
            <div className={classes.hero}>
                <span className={classes.title}>{data.name}</span>
                <div className={classes.icon}>
                    <Icon
                        size='lg'
                        iconPosition='after'
                        data={Number(data.price)}
                        src='/icon-ruble-white.svg'
                        withLabel
                    />
                </div>
            </div>
            <div className={classes.bg}></div>
            <div className={classes.page}>
                <div className={classes.tags}>
                    <Tag variants='secondary' text={`${data.year} курс`} />
                </div>
                <div className={classes.descriptions}>
                    <span className={classes.descriptions__title}>
                        Описание
                    </span>
                    <span className={classes.descriptions__text}>
                        {data.description}
                    </span>
                </div>
                <div className={classes.wrapper}>
                    <div className={classes.left}>
                        <div className={classes.subjects}>
                            <span className={classes.subjects__title}>
                                Предметы
                            </span>
                            <div className={classes.subjects__tags}>
                                {data.subjects.length > 0
                                    ? data.subjects.map((subject) => (
                                          <Tag
                                              key={subject}
                                              text={subject}
                                              variants='subject'
                                          />
                                      ))
                                    : ""}
                            </div>
                        </div>
                        <div className={classes.file}>
                            <span className={classes.file__title}>Файлы</span>
                            <div className={classes.fiel__download}>
                                {data.file ? (
                                    <a
                                        href={data.file}
                                        target='_blank'
                                        rel='noopener noreferrer'
                                    >
                                        Скачать файл
                                    </a>
                                ) : (
                                    "Нет файла"
                                )}
                            </div>
                        </div>
                    </div>
                    <div className={classes.right}>
                        <div className={classes.services}>
                            <span className={classes.services__title}>
                                Вид услуги
                            </span>
                            <div className={classes.services__tags}>
                                {data.services.length > 0
                                    ? data.services.map((services) => (
                                          <Tag
                                              key={services}
                                              text={services}
                                              variants='type'
                                          />
                                      ))
                                    : ""}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>

        // <div className={classes.div}>
        //     <h1>{data.name}</h1>
        //     <p>
        //         <strong>Описание:</strong> {data.description}
        //     </p>
        //     <p>
        //         <strong>Цена:</strong> {data.price}
        //     </p>
        //     <p>
        //         <strong>Год:</strong> {data.year}
        //     </p>
        //     <p>
        //         <strong>Статус:</strong>{" "}
        //         {data.isFinished ? "Завершено" : "Не завершено"}
        //     </p>
        //     <p>
        //         <strong>Файл:</strong>{" "}
        //         {data.file ? (
        //             <a
        //                 href={data.file}
        //                 target='_blank'
        //                 rel='noopener noreferrer'
        //             >
        //                 Скачать
        //             </a>
        //         ) : (
        //             "Нет файла"
        //         )}
        //     </p>
        //     <p>
        //         <strong>Пользователь:</strong> {data.user}
        //     </p>
        //     <p>
        //         <strong>Исполнитель:</strong> {data.executorId ?? "Не указан"}
        //     </p>
        //     <p>
        //         <strong>Предметы:</strong>{" "}
        //         {data.subjects.length > 0
        //             ? data.subjects.join(", ")
        //             : "Нет предметов"}
        //     </p>
        //     <p>
        //         <strong>Услуги:</strong>{" "}
        //         {data.services.length > 0
        //             ? data.services.join(", ")
        //             : "Нет услуг"}
        //     </p>
        //     <p>
        //         <strong>Дата создания:</strong>{" "}
        //         {data.createdAt.toLocaleDateString()}
        //     </p>
        //     <p>
        //         <strong>Слаг:</strong> {data.slug}
        //     </p>
        // </div>
    )
}
