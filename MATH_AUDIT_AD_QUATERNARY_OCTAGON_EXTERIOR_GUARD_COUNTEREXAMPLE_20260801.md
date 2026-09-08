# Exterior union and residence guards of the collared quaternary octagon

Date: 2026-08-01  
Lane: AD, adversarial OR-guard audit  
Status: exact local interface and literal counterexample.  This note does
not address common-cap compilation or existence of a global host factor.

## 0. Outcome

The long component created by the quaternary octagon has a genuinely
bounded exterior union interface: its distinct nonempty prefix-union and
suffix-union decks have four states each, independently of the residence
depth `h`.

Subject to ordinary off-end cleanliness of the two exterior fragments, the
residence condition at the two joins is also exact.  It is a pair of nested
labelled rays of length `h`.  These rays are necessary and sufficient for
the runs that cross a join; they cannot in general be replaced by finitely
many unlabelled endpoint bits.

This does **not** give a collar-only arbitrary-width transparency theorem
for the full one-path splice.  The splice transposes the two unchanged
donor subpaths.  Its complete crossing deck has a constant number of
ray/rectangle *families*, but two of those rays are arbitrary donor-path
decks and may contain `Theta(m)` distinct states.  More decisively, at
`m=5,h=1` there are two simple Johnson words on the same sixteen owners,
related by the exact quaternary toggle, such that

* both joins of the new collared component satisfy residence two;
* the octagon preserves lower, upper, typed-tail and typed-head resources
  exactly; but
* one old rank-seven interval union is absent from the new word.

Thus the correct positive statement is conditional: complete donor rays
and their crossing rectangles must be carried as guards.  The collar alone
does not generate them.

## 1. The exact four-state interface

Use the notation of
`MATH_THEOREM_AD_ENDPOINT_PATH_BANK_QUATERNARY_OCTAGON_20260801.md`.
Thus `S` has size `m-2`,

\[
 A_i=S+z+a_i,\qquad B_i=S+a_i+a_{i+1},                 \tag{1.1}
\]

and the return rail has core

\[
 Z=S+a_0+a_1+z+y.                                      \tag{1.2}
\]

Write its vertices, in the direction from `B_0` to `A_0`, as

\[
 B_0=V_1,V_2,\ldots,V_{h+2},V_0=A_0.                  \tag{1.3}
\]

The new long collared component is the word

\[
 \mathcal X=(A_1,V_1,V_2,\ldots,V_{h+2},V_0,B_3).     \tag{1.4}
\]

Put

\[
                         Q=Z+a_3.                      \tag{1.5}
\]

For a word `W`, let `P(W)` and `S(W)` denote its sets of nonempty
prefix unions and suffix unions.

### Theorem 1.1 (exact exterior union state)

For every admissible `1<=h<=m-2`,

\[
\begin{aligned}
 \mathcal P(\mathcal X)={}&
 \{Z-\{a_0,y\},\ Z-y,\ Z,\ Q\},\\
 \mathcal S(\mathcal X)={}&
 \{S+a_0+a_3,\ S+a_0+a_3+z,\ Q-a_1,\ Q\}.
                                                               \tag{1.6}
\end{aligned}
\]

In particular the total union is `Q`, and reversing the component merely
interchanges the two four-state decks.

#### Proof

The first owner is

\[
 A_1=Z-\{a_0,y\}.
\]

Adding `B_0` supplies `a_0`, giving `Z-y`.  The next rail owner `V_2`
supplies `y`; the first two owners already supply the two labels missing
from `V_2`, so the third prefix has union `Z`.  No later rail owner changes
that union, and the final owner `B_3` adds only `a_3`.  This proves the
prefix row.

From the right, the first two suffixes are `B_3=S+a_0+a_3` and
`A_0\cup B_3=S+a_0+a_3+z`.  The last rail owner before `A_0` supplies
`y` but misses `a_1`, giving `Q-a_1`.  Its predecessor supplies `a_1`,
giving `Q`; all longer suffixes stay there.  This proves (1.6).  \(\square\)

Thus intervals entering (1.4) from one side see only four collar states,
and intervals traversing it see only the one total state `Q`.

## 2. Exact residence state at the two joins

Let the minimum permitted positive-run length be

\[
                         \rho=h+1.                     \tag{2.1}
\]

Use the rotating-hole labels `x_0,...,x_(h-1)` from the rail.  The only
positive runs of (1.4) which can be too short after attachment are its
leading and trailing runs.  Their exact lengths are

\[
\begin{array}{c|c|c}
\text{coordinate}&\text{leading length}&\text{trailing length}\\ \hline
z&1&0\\
a_3&0&1\\
x_j&j+2&h-j+1\quad(0\le j<h).
\end{array}                                               \tag{2.2}
\]

Every other boundary-positive run either already has length at least
`rho`, is whole-component, or is zero.  The internal `y`-run has length
exactly `rho`.

Number exterior owners by their distance `t=1,...,h` from the join.  Define

\[
 \Lambda_t=\{z,x_0,\ldots,x_{h-t-1}\},\qquad
 \mathrm P_t=\{a_3,x_t,\ldots,x_{h-1}\},               \tag{2.3}
\]

where an inverted `x` interval is empty.

### Theorem 2.1 (necessary and sufficient join rays)

Assume neither join is a global word endpoint, both exterior words are
internally resident, and every exterior run ending at a collar endpoint on
a coordinate absent from that collar endpoint has length zero or at least
`rho`.  Attaching a left exterior word `L` and a right exterior word `R`
creates no short positive run at either join if and only if

\[
 \Lambda_t\subseteq L_{-t},\qquad
 \mathrm P_t\subseteq R_t\qquad(1\le t\le h),           \tag{2.4}
\]

where `L_(-t)` is the owner `t` positions before `A_1` and `R_t` is the
owner `t` positions after `B_3`.  If an exterior global endpoint is reached
before distance `t`, the corresponding condition is omitted because that
run is clipped.  The cleanliness hypothesis is exactly the separate
condition for coordinates absent from `A_1` or `B_3`; (2.4) controls all
and only the runs positive on both sides of a join.

#### Proof

The deficit of the leading `z`-run is `h`; the deficit of the leading
`x_j`-run is `h-j-1`.  Hence the owner at left distance `t` must contain
exactly all coordinates whose deficit is at least `t`, namely `Lambda_t`.
Failure at the first such position terminates a positive run below `rho`;
inclusion through the full deficit extends it to at least `rho`.

On the right, the deficits are `h` for `a_3` and `j` for `x_j`, yielding
`P_t`.  The same argument applies.  Formula (2.2) exhausts the possibly
short runs entering the collar; the off-end cleanliness hypothesis handles
exactly the exterior runs terminated by a zero at the collar endpoint.
Together these cases prove necessity and sufficiency.  \(\square\)

The number of **rays** is two, independent of `h`; the labelled ladder
inside each ray has length `h`.

## 3. What remains constant for the complete splice

After the octagon toggle, partition the affected part of the one path into
four consecutive blocks

\[
                       W^+=\mathcal X\,D\,E\,F,         \tag{3.1}
\]

where `D` is the remainder of the old `B_3`--`A_2` subpath, `E` is the old
`B_1`--`A_3` subpath, and `F` begins with `B_2` (or is absorbed into the
right exterior context).  For any interval beginning in block `i` and
ending in block `j>i`, its union is

\[
 S_i\ \cup\ Q_{i+1}\cup\cdots\cup Q_{j-1}\ \cup\ P_j,
                                                               \tag{3.2}
\]

where `S_i` is one suffix-union state of the first block, `P_j` is one
prefix-union state of the last block, and `Q_k` is the total union of an
intervening block.

Consequently four blocks have exactly six ordered crossing-rectangle
families, one for each pair `i<j`, in addition to their four internal decks.
This is `O(1)` families.  However (1.6) controls only the rays belonging to
`X`.  The prefix/suffix rays of `D` and `E` are arbitrary, and can have
linearly many distinct states.  Calling a complete arbitrary ray one
"ticket" is a legitimate conditional interface; calling the collar itself
a bounded complete ticket is not.

There is a stronger distinction between a bounded number of rectangles and
a bounded number of nested rays.

### Proposition 3.1 (a crossing rectangle needs linearly many rays)

Let the ground set have size `2m`, and let `Q` be the total collar union,
so `|Q|=m+3`.  For every

\[
                         2r\le m-3,                    \tag{3.3}
\]

there are two legal rank-`m` Johnson path pieces whose suffix and prefix
states, after union with `Q`, contain chains

\[
 Q\subset Q+v_1\subset\cdots\subset Q+v_1+\cdots+v_r
                                                               \tag{3.4}
\]

and

\[
 Q\subset Q+w_1\subset\cdots\subset Q+w_1+\cdots+w_r,          \tag{3.5}
\]

where the two new-label banks are disjoint.  Their crossing rectangle
contains all

\[
 Q+\{v_1,\ldots,v_i\}+\{w_1,\ldots,w_j\},qquad
                         0\le i,j\le r.                \tag{3.6}
\]

The inclusion poset in (3.6) is the product `[0,r] x [0,r]` and needs at
least `r+1` nested rays to cover it.  Consequently the full arbitrary
donor-path crossing interface cannot be represented by `O(1)` nested rays.

#### Proof

Choose disjoint banks `V={v_1,...,v_r}` and `W={w_1,...,w_r}` outside
`Q`, possible by (3.3).  Fix `s in S` and put

\[
 T=(A_1-\{s\})+a_0,\qquad T'=(B_3-\{s\})+z.           \tag{3.7}
\]

Thus `T` and `T'` lie in `Q` and are Johnson-adjacent to the respective
collar endpoints `A_1` and `B_3`.  Choose distinct `u_i in T` and
`u'_i in T'`.  The sets

\[
 T_i=(T-\{u_1,\ldots,u_i\})+\{v_1,\ldots,v_i\},\qquad
 T'_i=(T'-\{u'_1,\ldots,u'_i\})+\{w_1,\ldots,w_i\}    \tag{3.8}
\]

`T+{v_1,...,v_i}`; reversing the first path realizes this list as suffix
states, and the second realizes the `w` list as prefix states.  The last
left owner `T_0` joins `A_1`, and `B_3` joins the first right owner `T'_0`,
so these are literal exterior pieces, not detached abstract paths.  Union
with the intervening total state `Q` yields (3.4)--(3.6).

The masks with `i+j=r` are pairwise incomparable, so any cover by nested
chains has at least `r+1` members.  Conversely the `r+1` columns (or rows)
cover the product by chains, so this is the correct linear scale; only the
lower bound is needed.  \(\square\)

Thus the precise answer is:

* the packet has `O(1)` **rectangle families**;
* the collar itself has `O(1)` union states; but
* arbitrary donor rectangles do not reduce to `O(1)` nested rays.

## 4. A literal resident-join counterexample

Take `m=5,h=1` on the ten labels `0,...,9`, and put

\[
\begin{gathered}
 S=\{0,1,2\},\quad x_0=0,\\
 z=3,\ a_0=4,\ a_1=5,\ a_2=6,\ a_3=7,\ y=8,\ p=9.
                                                               \tag{4.1}
\end{gathered}
\]

The opened old collar and the new long collar are

\[
\begin{aligned}
 C={}&(01245,12458,12348,01234),\\
 X={}&(01235,01245,12458,12348,01234,01247).            \tag{4.2}
\end{aligned}
\]

Here and below a string denotes its set of digits.  Let

\[
\begin{aligned}
 J={}&12345,\\
 P_1={}&(01256,01257,01279,12379,01237),\\
 P_2={}&(01247,01278,01238,01236),\\
 B_2={}&01267.                                         \tag{4.3}
\end{aligned}
\]

Define the two owner words

\[
\begin{aligned}
 W^-={}&J\ C\ (01235)\ P_1\ P_2\ B_2,\\
 W^+={}&J\ X\ (01278,01238,01236)\ P_1\ B_2.          \tag{4.4}
\end{aligned}
\]

### Theorem 4.1 (collar-only bounded transparency is false)

The words in (4.4) have the following properties.

1. Each has length sixteen, has sixteen distinct rank-five owners, and
   consecutive owners are Johnson-adjacent.
2. They have exactly the same owner set.
3. The selected old support has the old collar-closing arc together with
   the three displayed path arcs, while the new word displays the four new
   octagon arcs.  These are respectively

   \[
   A_i\mathbin{\to}B_i\quad\hbox{and}\quad
   A_i\mathbin{\to}B_{i-1},
   \]

   so the lower, upper, tail and head resource sets agree exactly.
4. At residence threshold two, both exterior joins of `X` are legal.
5. The rank-seven mask

   \[
                         M=0123479                       \tag{4.5}
   \]

   is an interval union of `W^-` but not of `W^+`.

#### Proof

Direct comparison of consecutive five-sets in (4.4) proves Johnson
adjacency.  The old path order contains the arcs

\[
 A_1B_1,\quad A_3B_3,\quad A_2B_2,
\]

whereas the new order contains

\[
 A_1B_0,\quad A_0B_3,\quad A_2B_1,\quad A_3B_2.
\]

Together with the selected support's old collar-closing arc `A_0B_0` (opened in the
linear word `W^-`), these are exactly the two phases of the quaternary
octagon.  Its four-resource identity proves item 3, while inspection gives
items 1 and 2.  Thus the seam used to linearize the old cycle is not being
silently counted as one of the four exchanged resources.

For `h=1`, (2.3) gives `Lambda_1={z}` and `P_1={a_3}`.  The left neighbour
`J=12345` contains `z=3`; the right neighbour `01278` contains `a_3=7`.
The only coordinate present at `J` and absent from `A_1` is `a_0=4`; its
run reaches the global left endpoint and remains clipped.  On the right,
the only coordinate absent from `B_3` which starts positively is `y=8`,
and it persists through the first two owners.  Thus the off-end cleanliness
hypothesis also holds, and Theorem 2.1 proves item 4.

In `W^-`, the consecutive interval

\[
                     (12379,01237,01247)
\]

has union `M`.  In `W^+`, the private label `p=9` occurs only in the two
owners `01279,12379`, both lying in `P_1`, while `a_0=4` occurs only before
`P_1`.  Every new interval containing both `9` and `4` traverses `P_2` and
therefore contains `y=8`.  Since `8` is not in `M`, no new interval has
union `M`.  This proves item 5.  \(\square\)

Reversing both words and applying a dihedral relabelling of the four
`a_i` transports the fixture to every equivalent choice of global
orientation and octagon indexing.  Hence those choices do not repair the
universal claim.

## 5. Exact boundary

What is proved is

\[
\boxed{
\begin{array}{c}
\text{the collared long component exports four union states per side,}\\
\text{and exact join residence is two nested labelled rays;}\\[2mm]
\text{the full splice requires additional donor-ray/rectangle guards.}
\end{array}}
\]

The counterexample refutes the local implication

\[
 \text{local octagon four-resource equality + collar rays + join residence}
 \quad\Longrightarrow\quad
 \text{arbitrary-width OR coverage preservation}.              \tag{5.1}
\]

It does not refute a conditional theorem which exports the complete
prefix/suffix decks of both donor subpaths and checks all six crossing
rectangles in (3.2).  It also makes no claim about common-cap compilation,
which remains a separate guard.  In particular, the displayed sixteen-edge
words are not globally lower/upper-rainbow factors; no counterexample inside
the fixed-`H` exact-factor class is claimed.

## 6. Independent replay

Run

```text
python3 scratch/audit_ad_quaternary_octagon_exterior_guard_counterexample_20260801.py
```

The dependency-free replay checks the exact four-state interface and
boundary-run table in 35 cases, literal Johnson realizations of the product
rectangle in ten dimensions, its antidiagonal ray-width lower bound, and
the sixteen-owner lost-mask fixture.  It reports status
`PASS_AD_QUATERNARY_OCTAGON_EXTERIOR_GUARD_COUNTEREXAMPLE`.
