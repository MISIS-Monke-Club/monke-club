import { useQuery } from "@tanstack/react-query"
import { ReactNode } from "react"
import { useDebouncedCallback } from "use-debounce"
import { getMentorsList } from "../api"
import classes from "./mentors-list.module.scss"
import { ItemsList } from "@shared/ui/items-list"
import { MentorCard, MentorModel } from "@entities/mentor"
import { Input } from "@shared/ui/input"
import { useQueryPrams } from "@shared/lib/params-parser"
import {
    SheetTrigger,
    SheetContent,
    SheetHeader,
    SheetTitle,
    SheetDescription,
    Sheet,
} from "@shared/ui/sheet"
import { Button } from "@shared/ui/button"

const mentorsMaper = (elements: MentorModel[]): ReactNode => (
    <>
        {elements.map((el) => (
            <MentorCard key={el.username} mentor={el} />
        ))}
    </>
)

export function MentorsList() {
    const { addParams, params, deleteParams } = useQueryPrams()
    const search = params.get("search")?.toString()
    const course = params.get("course")?.toString()
    const { data = [], isLoading } = useQuery(
        getMentorsList({
            search,
            course,
        })
    )

    const handleChange = useDebouncedCallback((val: string) => {
        if (val.length !== 0) {
            addParams("search", val)
        } else {
            deleteParams("search")
        }
    }, 300)

    return (
        <div className={classes.mentorsList}>
            <div className={classes.actions}>
                <Input
                    className={classes.search}
                    placeholder='введите запрос...'
                    defaultValue={search}
                    onChange={(e) => handleChange(e.target.value)}
                />
                <Sheet>
                    <SheetTrigger className={classes.filters}>
                        <svg
                            width='60'
                            height='34'
                            viewBox='0 0 75 34'
                            fill='none'
                            xmlns='http://www.w3.org/2000/svg'
                        >
                            <path
                                d='M66.8944 6.61475H8.10575C7.13303 6.61475 6.34448 7.42316 6.34448 8.42039V8.42134C6.34448 9.41857 7.13303 10.227 8.10575 10.227H66.8944C67.8672 10.227 68.6557 9.41857 68.6557 8.42134V8.42039C68.6557 7.42316 67.8672 6.61475 66.8944 6.61475Z'
                                fill='#6B7B8F'
                            />
                            <path
                                d='M22.1481 15.6454C26.3874 15.6454 29.8241 12.2087 29.8241 7.96935C29.8241 3.73001 26.3874 0.293335 22.1481 0.293335C17.9087 0.293335 14.472 3.73001 14.472 7.96935C14.472 12.2087 17.9087 15.6454 22.1481 15.6454Z'
                                fill='#2F3A4A'
                            />
                            <path
                                d='M66.8944 23.7729H8.10575C7.13303 23.7729 6.34448 24.5814 6.34448 25.5786V25.5795C6.34448 26.5768 7.13303 27.3852 8.10575 27.3852H66.8944C67.8672 27.3852 68.6557 26.5768 68.6557 25.5795V25.5786C68.6557 24.5814 67.8672 23.7729 66.8944 23.7729Z'
                                fill='#6B7B8F'
                            />
                            <path
                                d='M53.7552 33.7067C57.9946 33.7067 61.4313 30.27 61.4313 26.0306C61.4313 21.7913 57.9946 18.3546 53.7552 18.3546C49.5159 18.3546 46.0792 21.7913 46.0792 26.0306C46.0792 30.27 49.5159 33.7067 53.7552 33.7067Z'
                                fill='#2F3A4A'
                            />
                        </svg>
                    </SheetTrigger>
                    <SheetContent>
                        <SheetHeader>
                            <SheetTitle>Фильтры и сортировки</SheetTitle>
                            <SheetDescription>
                                Тут вы можете выполнить фильтрацию
                            </SheetDescription>
                            Курс
                            <Button
                                onClick={() => {
                                    addParams("course", "1")
                                }}
                            >
                                1
                            </Button>
                            <Button
                                onClick={() => {
                                    addParams("course", "2")
                                }}
                            >
                                2
                            </Button>
                            <Button
                                onClick={() => {
                                    addParams("course", "3")
                                }}
                            >
                                3
                            </Button>
                            <Button
                                onClick={() => {
                                    addParams("course", "4")
                                }}
                            >
                                4
                            </Button>
                            <Button
                                onClick={() => {
                                    addParams("course", "5")
                                }}
                            >
                                5
                            </Button>
                            <Button
                                onClick={() => {
                                    addParams("course", "6")
                                }}
                            >
                                6
                            </Button>
                        </SheetHeader>
                    </SheetContent>
                </Sheet>
                {/* <Button className={classes.filters}></Button> */}
            </div>
            <ItemsList
                className={classes.list}
                elements={data}
                mapFunction={mentorsMaper}
                isLoading={isLoading}
            />
        </div>
    )
}
