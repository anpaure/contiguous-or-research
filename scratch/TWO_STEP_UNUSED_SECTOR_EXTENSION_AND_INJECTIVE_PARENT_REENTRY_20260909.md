# Two unused-sector steps and an injective parent re-entry

Date: 2026-09-09. Pure bounded construction and boundary audit; no execution,
search, or residual matching decision.

This applies to any selected subset of the actual-parent0P1 connectors,
including the complete mixed two-order bank. It constructs two further
age-legal steps through unused lower/upper owners, then identifies an
injective re-entry into the occupied parent copy and its exact remaining
age test. It does not assert a spanning factor or a legal global rethreading.

## 1. Parameters and retained input

Use a parent dimension2r+1 with lower rankr, r>=2; the child dimension is
2r+3 with lower rankr+1. Equivalently, if the parent is written2s−1 as in
the task statement, set r=s−1. This avoids changing the ranks of the existing
0P1 records.

Let sigma be a specified strict canonical-Phi parent factor of residence3.
Embed every parent state as0P1. Select h ports P=00D1, D Dyck of semilength
r−1. WriteD=1R. The [two-order connector theorem](TWO_ORDER_CANONICAL_PHI_CONNECTOR_AND_COMPLETE_0P1_PORT_BANK_20260909.md)
supplies a legal three-step route at every such port from the actual parent
history: use deletions b,a,d when age(a)>=2, otherwise b,d,a. At most one
of a,d can be freshly inserted, so the latter branch is legal.

I independently read that complete pure theorem: its first-minimum proof,
complementary exact age conditions, mixed-bank disjointness, and common
endpoint agree. The finite mixed-route counts have their separate run
certificate; no count is recomputed here.

Both routes end at

\[
E_D=1110R00.
\]

In coordinate order let u,x,y be its initial three ones, and a,b its final
two coordinates. At E_D their ages are exactly1,2,3 respectively, all
surviving R-ones have age at least4, and a,b are absent.

The existing path bank has `M+3h` used lower states and `M+2h` assigned edges
or consumed uppers, where `M=binom(2r+1,r)`. Its missing incoming heads are
`0sigma(00D1)1`. All embedded states haveu=0,b=1; all new connector lower
states haveb=0. These facts hold for both deletion orders.

## 2. A definite two-step extension through unused states

Append to every E_D the two edges

\[
\boxed{
1110R00\longrightarrow F_D=1100R01
\longrightarrow G_D=1000R11.}
\tag{2.1}
\]

The first insertion is b: every nonempty old prefix of1110R is positive,
and the final00 first reaches−1 atb. Delete y, whose age is exactly3.

At F_D the old prefix1100 has heights1,2,1,0 and R has prefix heights at
least−1. Thus the first new minimum−2 is reached at a, and canonical Phi
adds a. Delete x, whose age at F_D is exactly3. Both steps are therefore
legal for every actual incoming history supplied by either connector order.

The new states haveu=b=1, unlike every used lower state in the prior bank.
They are injectively indexed by D, and mutually separated by x: F_D hasx=1,
G_D hasx=0. Thus all2h new lower states are unused and mutually distinct.

The consumed uppers are

\[
1110R01,\qquad1100R11.
\]

They likewise haveu=b=1, whereas the prior embedded uppers haveu=0,b=1
and the prior newly consumed connector uppers haveb=0. Both new upper
banks are injective and separated by y. Equivalently their distinctness
follows from Phi injectivity on the distinct sources E_D,F_D.

The extended ledger is therefore

\[
\boxed{\text{used lowers}=M+5h,\qquad
\text{consumed uppers / assigned edges}=M+4h.}
\tag{2.2}
\]

There remainh open paths with the original missing heads, plus any untouched
parent components that had no selected cut. The two-step extension itself
has no new collision or age condition.

## 3. Exact new end and smaller matching copy

At G_D=1000R11 the boundary ages are

\[
\operatorname{age}(u)=3,\quad
\operatorname{age}(b)=2,\quad
\operatorname{age}(a)=1,
\]

and every R-one has age at least6. Its outgoing Phi is

\[
\boxed{\Phi(G_D)=1000\Phi_{2r-3}(R)11.}
\tag{3.1}
\]

Indeed R has length2r−3, rankr−2, final height−1 and minimum−1. The prefix
1000 shifts its walk down by2, and the last two ones cannot create the
first minimum. The smaller first-minimum matching therefore acts insideR.
This is another instance of the already known balanced-block embedding:
the fixed cyclic block is111000. It does not assert an available smaller
residence3 factor or amplify residence.

The exact immediate age-legal deletions at G_D are u and the R-ones.
Deleting a or b is forbidden. Deleting an R-one stays in the unused u=b=1
sector, subject to future inventory and age constraints that are not solved
here. The other legal option is the re-entry below.

## 4. An explicit injective re-entry, which requires another parent cut

Let Q=Phi_(2r−3)(R). Deleting u at G_D is legal at its exact age3 and gives

\[
G_D\longrightarrow H_D=0000Q11=0P'_D1,
\qquad P'_D=000Q1.
\tag{4.1}
\]

This is an occupied state of the complete embedded parent copy. Distinct D
give distinct R, and Phi is injective, so all P'_D and H_D are distinct.

Since R has minimum−1, Q has minimum0. Therefore P'_D has minimum exactly−3.
It is not a selected port `00 D_0 1`, whose third bit is1, whereas P'_D starts000.
It is also not an original missing incoming head's parent mask: a strict
successor of `00 D_0 1` is a facet of `01 D_0 1`, so its minimum is−1 when a is deleted
and−2 when a D_0-one is deleted.

Thus (4.1) cannot simply be installed on top of the existing incoming edge.
Its existing predecessor is `sigma^{-1}(P'_D)`, and that embedded parent
edge must be cut. These h predecessor states are distinct and are not any
originally selected port, since selected-port successors have minimum at
least−2. Their edges were therefore retained before this additional cut.

At the incidence level only, cutting those h edges and adding the h re-entry
edges keeps the ledger(2.2) unchanged. The missing incoming heads remain the
original `0sigma(00D)1`; the free outgoing ends become

\[
0\sigma^{-1}(P'_D)1,
\]

with their corresponding embedded parent Phi uppers. Overlaps between these
new cut tails and other path heads or re-entry states are not excluded.
The new incidence graph can therefore contain closed components; no global
component-merging assertion is made.

## 5. Re-entry ages and the exact first-two-step continuation gate

At H_D the newly inserted smaller matching coordinate c=Q\R has age1,
a has age2, b has age3, and every surviving R-coordinate has age at least7.
The removed u,x,y are absent. Consequently following the prescribed parent
successor from P'_D is residence3 legal exactly when

\[
\boxed{
\delta(P'_D)\notin\{a,c\},\qquad
\delta(\sigma(P'_D))\ne c,}
\tag{5.1}
\]

where \(\delta(T)=T\setminus\sigma(T)\) is the single parent deletion coordinate.
The first edge cannot delete age1 c or age2 a; the second cannot delete c
at age2. After these two steps all inherited surviving coordinates are
mature. Coordinates inserted during the retained parent trajectory obey
the parent's verified residence property. The permanent embedded b remains
present and is already mature.

Equation(5.1) is an exact local continuation test, not an assertion that the
specified parent satisfies it. If a path reaches another modified boundary
before those checks finish, the actual next edges and age obligations must
be checked instead. No execution of these tests or new cut is performed.

## 6. Why no age-legal augmentation of at most three edges closes the original ends

This gives an exact short-route boundary, without restricting to the
particular two-step choice(2.1). At E_D, u and x have ages1 and2, so the
first deletion must be a mature coordinate d in `{y} union R`. Every missing
head begins with child bits00. To clear both u and x in at most three
transitions, age3 forces the remaining deletions to be x second and u third.

The first insertion is b. After deleting d, the old word before a,b has
minimum at least−1 and final height−1; hence the second insertion is a.
After also deleting x, let Z be that old word. The original old word1110R
had every nonempty prefix at least1. Deleting two ones lowers a suffix by
at most4, so Z has minimum at least−3; its final height is−3, making the
minimum exactly−3. It still contains its first coordinate u.

The third Phi insertion raises that minimum to−2. Deleting u lowers every
nonempty old prefix by2, making the child old-segment minimum−4. Removing
the initial child zero to read the parent mask raises its relative heights
by1. Thus the resulting parent mask has minimum exactly−3. The trailing
a,b ones create no new lower minimum.

Every original missing head, by contrast, has a parent mask of minimum−1
or−2 as shown in Section4. Therefore **no age-legal route of at most three
extra transitions from an original E_D reaches any original missing head**.
This remains true before imposing the unused-state restriction. In
particular a three-edge augmentation through unused owners cannot close
these sockets. An exchange that additionally reassigns occupied parent
incidences is outside that restricted statement and requires its own
degree, age, and topology checks.

## 7. Stop boundary

The new proved construction is the simultaneous two-edge extension through
unused owners. The optional injective re-entry has exact extra-cut and
age requirements. Longer routes, a residual perfect matching, tests of
(5.1) on the actual parent, and new chronology choices have not been
searched for or executed. No spanning child factor or all-dimensional
equality follows from the local incidence ledger.
