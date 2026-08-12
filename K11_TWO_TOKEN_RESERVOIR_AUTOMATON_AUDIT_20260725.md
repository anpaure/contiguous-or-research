# Audited two-token reservoir automaton for the (K=11) equality case

Date: 2026-07-25

## 1. Scope and verdict

Assume the already audited endpoint-ordered normal form of a hypothetical
nonzero universal word of length (465).  Its middle-level quotient is a
union of six alternating paths.  Along one path write

\[
 S_0,D_0,S_1,D_1,\ldots,S_\ell,D_\ell,
\]

where (S_i,D_i\in\binom{[11]}5), (S_i\cap D_i=\varnothing), and let

\[
 a_i=[11]\setminus(S_i\cup D_i).
\]

For (0\le i<\ell), let (b_i) be the unique coordinate outside
(S_{i+1}\cup D_i).  Then

\[
 S_{i+1}=S_i-b_i+a_i,
 \qquad
 D_{i+1}=D_i-a_{i+1}+b_i.                       \tag{1.1}
\]

Put

\[
 B_i=S_i\cap S_{i+1}=S_i-b_i,
 \qquad
 Y_i=D_i\cap D_{i+1}=D_i-a_{i+1}.               \tag{1.2}
\]

The physical no-lazy conditions are

\[
 a_i\ne b_{i+1},\qquad a_i\ne b_{i+2},          \tag{1.3}
\]

whenever the indices exist.  The automatic state exclusions are
(a_i\ne b_{i-1},b_i).

This note proves that the entire interior dynamics are exactly a
two-token cache driven by a four-separated coordinate word.  It also gives
new exact consequences for shadow pairs and three-coordinate residence
runs.  It does **not** decide whether the length-(465) object exists.

One error in an agent summary was found during this audit.  The correct
lower-shadow recurrence is

\[
 \boxed{B_{i+1}=B_i-b_{i+1}+a_i},                \tag{1.4}
\]

not (B_i-a_i+b_{i+1}).  All statements below use (1.4).

## 2. Exact port residence

### Lemma 2.1 (four separation)

On each path, equal symbols in the (a)-word occur at index distance at
least five.  The same is true in the (b)-word.  Moreover

\[
 b_i\notin\{a_{i-2},a_{i-1},a_i,a_{i+1}\}.       \tag{2.1}
\]

#### Proof

At state (i), coordinate (a_i) is outside both (S_i,D_i).  The next
transition inserts it into (S_{i+1}).  Conditions (1.3) prevent its
deletion at the next two eligible transitions, so it remains in the source
through (S_{i+3}).  If it is deleted as early as possible, it enters the
target at state (i+4), and can become the missing coordinate again only
at state (i+5).  This proves the (a)-separation.  The same state cycle,
starting with the transition (S\to D) labelled (b_i), proves the
(b)-separation.

The middle two exclusions in (2.1) are the automatic and one-step physical
conditions; (b_i\ne a_{i-2}) is the two-step condition; and
(b_i\ne a_{i+1}) follows because (a_{i+1}\in D_i) whereas
(b_i\notin D_i).  \(□\)

### Theorem 2.2 (two-token reservoir automaton)

Fix an interior state (i\ge3), and put

\[
 x_0=a_{i-3},\quad x_1=a_{i-2},\quad
 x_2=a_{i-1},\quad x_3=a_i,
\]

\[
 R_i=S_i\setminus\{x_0,x_1,x_2\}.               \tag{2.2}
\]

Then the four (x_j)'s are distinct, (R_i) is a two-set disjoint from
them, and

\[
 \boxed{
 S_i=R_i\sqcup\{x_0,x_1,x_2\},\qquad
 U_i:=[11]\setminus D_i
     =R_i\sqcup\{x_0,x_1,x_2,x_3\}.}            \tag{2.3}
\]

For (i<\ell), the next missing coordinate

\[
 x_4=a_{i+1}
\]

is one of the five elements of (D_i), while

\[
 \boxed{b_i\in\{x_0\}\cup R_i.}                 \tag{2.4}
\]

The residual update is exactly

\[
 \boxed{
 R_{i+1}=
 \begin{cases}
 R_i,&b_i=x_0,\\
 (R_i\setminus\{b_i\})\cup\{x_0\},&b_i\in R_i.
 \end{cases}}                                    \tag{2.5}
\]

Conversely, the local rules (2.3)--(2.5), together with
(x_4\in D_i), imply both physical exclusions in (1.3).

#### Proof

The coordinate (a_{i-j}) enters the source one step after it is missing.
Lemma 2.1 prevents the three coordinates (x_0,x_1,x_2) from having left
by state (i).  They lie in (S_i), while (x_3=a_i) is the missing
coordinate.  This proves (2.2)--(2.3).

The second recurrence in (1.1) shows that (a_{i+1}\in D_i).  Also
(b_i\in S_i).  Equation (2.1) excludes (x_1,x_2), leaving exactly the
three possibilities in (2.4).  Substituting these alternatives into
(S_{i+1}=S_i-b_i+x_3), then removing the new recent triple
(x_1,x_2,x_3), gives (2.5).

Conversely, (2.4) says (b_i\ne a_{i-2},a_{i-1}).  After shifting the
index, these are precisely (a_j\ne b_{j+2},b_{j+1}).  \(□\)

The two shadow colors are now explicit:

\[
 \boxed{
 Y_i=[11]\setminus
 \bigl(R_i\cup\{x_0,x_1,x_2,x_3,x_4\}\bigr),}   \tag{2.6}
\]

and

\[
 \boxed{
 B_i=
 \begin{cases}
 R_i\cup\{x_1,x_2\},&b_i=x_0,\\
 \{x_0,x_1,x_2\}\cup(R_i\setminus\{b_i\}),
     &b_i\in R_i.
 \end{cases}}                                    \tag{2.7}
\]

Both follow directly from (1.2).  Moreover, the exact inclusion matching
implies that the (462) sets (S_i) enumerate all five-sets and the
(462) sets (U_i) enumerate all six-sets.  Thus the remaining physical
gate is a universal two-token sliding-window system, not merely a local
necessary condition.

## 3. Coupled shadow walks

Equations (1.1)--(1.2) give

\[
 B_{i+1}=B_i-b_{i+1}+a_i,                        \tag{3.1}
\]

\[
 Y_{i+1}=Y_i-a_{i+2}+b_i,                        \tag{3.2}
\]

where (3.2) is lazy exactly when (a_{i+2}=b_i).  Hence (B) is a
nonlazy walk in (J(11,4)), while (Y) is a possibly lazy walk.
Every lower edge union is the globally unique source state (S_{i+1}),
and every nonlazy upper edge union is the globally unique target state
(D_{i+1}).

### Lemma 3.1 (short-repeat exclusion)

Along one path, a fixed (B)-color cannot recur at index distance one,
two, or three.

#### Proof

Distance one is lower physical nonlaziness.  At distance two, the two
Johnson edges traverse the same unordered pair of (B)-vertices in reverse
order, so their unions would give (S_{i+1}=S_{i+2}).

At distance three, the three consecutive Johnson edges close a triangle.
Every triangle in (J(11,4)) is either a top triangle (three four-sets in
one five-set) or a bottom triangle (three four-sets over one common
three-set).  The first repeats a source union.  The second makes two
consecutive rank-three intersections equal, contradicting the second
physical exclusion.  \(□\)

### Theorem 3.2 (turn-pair injectivity)

The occurrence map

\[
 i\longmapsto(B_i,Y_i)                           \tag{3.3}
\]

is injective.

#### Proof

At one turn,

\[
 [11]=B_i\sqcup Y_i\sqcup\{a_i,b_i,a_{i+1}\},   \tag{3.4}
\]

and the three displayed coordinates are distinct.  For fixed (B,Y),
their complement is therefore a fixed three-set (T).  The occurrence
uses the (B)-colored source edge joining (B+a_i) to (B+b_i), a
two-subset of (T).

All edges of one fixed (B)-color form a matching on the seven source
supersets of (B): if two shared a source vertex, they would be the two
consecutive path edges there and would have equal adjacent (B)-colors.
But any two two-subsets of the three-set (T) intersect.  Hence two
occurrences with the same pair ((B,Y)) are impossible.  \(□\)

Consequently

\[
 \mu_B(B)\le3,\qquad \mu_Y(Y)\le6.               \tag{3.5}
\]

The first bound is the matching number of seven source supersets.  The
second follows because the (Y)-colored target edges form a linear forest
on the seven target supersets of (Y).

## 4. Exact endpoint marginals

For a coordinate (x), let

* (p_x) be the number of paths whose initial source contains (x);
* (s_x) be the number whose terminal target contains (x);
* (u_x) be the number whose initial missing label is (x);
* (t_x) be the number whose terminal missing label is (x).

Every coordinate is the missing label at exactly (42) states.  Summing
the source recurrence over all paths gives

\[
 \boxed{\#\{i:b_i=x\}=36+p_x+s_x.}               \tag{4.1}
\]

The number of source and target residence runs of (x) are respectively

\[
 R_x^S=42-t_x+p_x,\qquad R_x^D=42+s_x-u_x.        \tag{4.2}
\]

Since (x) belongs to exactly (210) source states and (210) target
states,

\[
 \boxed{
 \deg_B(x)=168+t_x-p_x,\qquad
 \deg_Y(x)=168+u_x-s_x.}                         \tag{4.3}
\]

These formulas were rederived from both (1.1) and binary-run counting;
the two derivations agree.

## 5. Higher-order residence identities

For nonempty (Q\subseteq[11]), (|Q|=r\le5), let (R_S(Q)) be the
total number of runs, over all six paths, of the predicate (Q\subseteq
S_i).  Define (R_D(Q)) analogously.  Then

\[
 \boxed{
 \sum_{\substack{T\supseteq Q\\|T|=4}}\mu_B(T)
 =\binom{11-r}{5-r}-R_S(Q),}                     \tag{5.1}
\]

\[
 \boxed{
 \sum_{\substack{T\supseteq Q\\|T|=4}}\mu_Y(T)
 =\binom{11-r}{5-r}-R_D(Q).}                     \tag{5.2}
\]

Indeed, the binomial coefficient is the number of five-set states
containing (Q), and each true run of length (L) contributes (L-1)
adjacent intersections containing (Q).

At (r=4),

\[
 \mu_B(Q)=7-R_S(Q),\qquad
 \mu_Y(Q)=7-R_D(Q),                              \tag{5.3}
\]

and

\[
 \sum_{|Q|=4}R_S(Q)=\sum_{|Q|=4}R_D(Q)=1854.     \tag{5.4}
\]

Thus the two support-(319) conditions say exactly that at most eleven
four-sets have seven source runs, and at most eleven have seven target
runs.

### Theorem 5.1 (three-set run cap)

For every three-set (Q), every run of (Q\subseteq S_i) has length at
most three.  Consequently

\[
 R_S(Q)\ge10,
 \qquad
 \sum_{\substack{B\supset Q\\|B|=4}}\mu_B(B)\le18.              \tag{5.5}
\]

#### Proof

If four consecutive source states contained (Q), then the three
intervening (B)-colors would be distinct four-sets containing (Q).
The first two intersect in (Q), and so do the last two.  These are two
consecutive equal rank-three colors, forbidden by physicality.  Since
there are (\binom82=28) source states containing (Q), at least
(\lceil28/3\rceil=10) runs are necessary.  Equation (5.1) then gives
the second assertion.  \(□\)

If (z_1) is the number of one-state path components and (N_j) denotes
the total number, over all three-sets (Q), of (Q\)-runs of length (j),
then every run has (j\le3) and exact double counting gives

\[
 \boxed{
 N_1=1422+z_1,\qquad
 N_2=924-2z_1,\qquad
 N_3=450+z_1.}                                  \tag{5.6}
\]

To verify (5.6), note that the total number of three-set truths is
(462\binom53=4620), the total number of runs is
(165\binom82-456\binom43=2796), and every physical three-state source
intersection is one three-set.  The number of such windows is
(450+z_1), which is exactly (N_3).

## 6. What the new constraints do and do not prove

The disjointness bipartite graph between two copies of
(\binom{[11]}4) is (35)-regular.  It therefore has two edge-disjoint
perfect matchings.  One complete matching plus any (126) edges of the
second gives (456) distinct disjoint pairs ((B,Y)), full support
(330/330), and degrees only one or two.  Hence totals, disjointness,
support, pair injectivity, and multiplicity caps alone are mutually
consistent.

The new obstruction is genuinely temporal.  A survivor must simultaneously

1. traverse all five-sets as (R_i) plus the previous three (a)-symbols;
2. traverse all six-sets as (R_i) plus the previous four (a)-symbols;
3. obey the two-token update (2.5) across six path cuts; and
4. attain support at least (319) in both explicit color formulas
   (2.6)--(2.7).

No contradiction or length-(465) construction is currently known.  The
current exact interval therefore remains

\[
 \boxed{465\le\nu(11)\le477.}
\]

