# Height-adaptive PBBS construction: explicit polynomial rate and a24,957 word

**Later record update:** the construction and proof below are retained
unchanged. The strongest current estimate of this same construction is
the [explicit harmonic-period rate](/Users/amir.nuriyev/Documents/problem/HEIGHT_ADAPTIVE_HARMONIC_PERIOD_RATE_20260908.md).
The supplied [24,658-letter word](/Users/amir.nuriyev/Documents/problem/K17_UPPER24658_VERIFIED_20260908.md)
is independently verified, leaving a 345-position gap. Lengths and gaps
below describe this earlier 24,957 construction, not the current record.

Date: 2026-09-08. The user's new finite construction and strict-height
refinement have completed internal proof review, including an independent
check of the interleaved-cycle height. The argument uses the retained
finite PBBS matching/corridor identities. It does not use the proposed
asymptotic coefficient-one theorem, the clock estimates, renewal process,
overlap bounds, or any of the logarithmic-rate arguments.

These are internal mathematical reviews, not external or formal
certification. The explicit finite word below has additionally passed
independent exhaustive target verification.

## 1. The general finite theorem

For every odd n=2r+1>=3, with W_r=binom(2r+1,r),

\[
\boxed{\displaystyle
 \nu(2r+1)\le W_r+
      \left\lfloor\frac{2^{2r+2}-3W_r}{2r+1}\right\rfloor.}
\tag{1}
\]

The exact trimmed lift gives the even-dimensional bound

\[
\boxed{\displaystyle
 \nu(2r+2)\le2W_r+
        2\left\lfloor\frac{2^{2r+2}-3W_r}{2r+1}\right\rfloor.}
\tag{2}
\]

In particular,

\[
 \nu(k)\le W(k)\left(1+\sqrt{\frac{2\pi}{k}}+O(k^{-1})\right),
 \qquad 0\le\nu(k)-B(k)=O\!\left(\frac{W(k)}{\sqrt k}\right).
\tag{3}
\]

The verified integer thresholds are

\[
 \nu(k)<1.1W(k)\quad(k\ge569),\qquad
 \nu(k)<1.01W(k)\quad(k\ge62233).                     \tag{4}
\]

These are guarantees for all dimensions past the thresholds, not claims
about the earliest dimension where the true optimum has those ratios.
The bounds have no unspecified constants in (1), (2) or (4).

## 2. The actual finite construction

On rank-r binary states of length n, let f complement every bit except
the unique unmatched zero in clockwise10 matching, and put g=f².
Decompose the permutation g into its cycles. For one cycle write

    A_i=g^i A_0,  X_i=[n]\A_i,  i modulo v,

and let h be its invariant normalized Dyck height. It satisfies1<=h<=r.
Form the nonzero letters

\[
 D_i=\bigcap_{j=0}^{h}X_{i+j}.                              \tag{5}
\]

Emit one period of D followed by its first2h-1 letters. Concatenate these
blocks over all cycles in any fixed order. The exact length is

\[
 N_r=W_r+\sum_{\mathcal C}(2h_{\mathcal C}-1).              \tag{6}
\]

Every cycle uses its own height. No residence repair, exterior word,
probabilistic cutoff or asymptotic diagonal choice occurs in this recipe.

## 3. Why the strict-height corridor covers all ranks

The retained finite global-maximum corridor lemma is
[Lemma21.1 and Theorem21.2](/Users/amir.nuriyev/Documents/problem/PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md:2117).
For a rank-(r-q) target S, its forward and reverse unmatched-zero marks
number d=2q+1. In expanded order a shared coordinate has order C_x,A_x.
If z_i counts forward marks between successive reverse marks, the cyclic
potential has increments z_i-1. Every global maximum supplies the actual
corridor

\[
 B_t=S\cup\{C_0,\ldots,C_{q-t-1}\}
       \cup\{A_0,\ldots,A_{t-1}\},\qquad
 gB_t=B_{t+1},\quad\bigcap_{t=0}^{q}B_t=S.                 \tag{7}
\]

For nonempty S the maximum can be chosen just after a nonempty physical
reverse-Dyck gap. If the preceding gap were empty, its two reverse marks
would be adjacent zeros and the expanded gap would contain at most one
forward mark. Maximality forces exactly one, so the preceding reverse
mark is another global maximum. Moving backward across empty gaps must
eventually reach a nonempty gap, since S is nonempty.

That gap has a negative prefix minimum. Its suffix after that minimum
rises by at least one. In B_0 the next q selected reverse marks are ones;
the intervening reverse gaps have total increment zero. The resulting
proper cyclic segment rises by at least q+1. The largest proper cyclic
rise of a deficit-one middle state is exactly its normalized Dyck height.
Thus this actual corridor satisfies

\[
                         h(B_0)\ge q+1.                   \tag{8}
\]

The restriction S nonempty is essential: q=r would demand an impossible
height r+1. For q=0 any one-state corridor has height at least one.

There is also no hidden change of height on interleaving. If D=P1Q at
its first step reaching height H, the exact one-step rooted map is
complement(Q)0complement(P). Along its first part the height is H minus
the old height in Q, reaching H at the end; the remaining part stays
between0 and H-1. Hence f, f^-1 and g all preserve H exactly.

For a lower target use the interleaved owners
Y_j=(f^-1g^jB_0)^c, j=0,...,q+1. They have the same height and
Y_j intersection Y_(j+1)=B_j. Therefore S is the intersection of
q+2 consecutive owners in a component with h>=q+1. For an upper target
S^c, (7) directly gives a union of q+1 complementary owners.

[The complete strict-height and interleaving proof](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_STRICT_HEIGHT_CORRIDOR_AND_INTERLEAVED_HEIGHT_INDEPENDENT_AUDIT_20260908.md)
checks the actual global-max boundary, shared labels, proper cyclic
segment, all boundary cases and exact finite source identities.

## 4. Nonempty erosion and ordinary interval witnesses

The finite marked-step identities give the residence margin. A newly
born up-step has height1; before its consuming update it reaches h.
If its nonconsuming visits to the P,R,S pieces number N_P,N_R,N_S,
then1+N_P-N_R=h and

    T=1+N_P+N_R+N_S=h+2N_R+N_S>=h.

The complementary owner residence has length T+1. Thus every bounded
positive coordinate run of X has length at least h+1. Permanent positive
coordinates satisfy the same erosion identities automatically.

Consecutive owners are Johnson neighbors, so |D_i|>=r+1-h>=1.
Checking each positive run gives the exact identities

\[
 X_a=\bigcup_{i=a-h}^{a}D_i,\qquad
 \bigcap_{j=0}^{p-1}X_{a+j}
      =\bigcup_{i=a+p-1-h}^{a}D_i\quad(1\le p\le h+1),
\tag{9}
\]

\[
 \bigcup_{j=0}^{p-1}X_{a+j}
      =\bigcup_{i=a-h}^{a+p-1}D_i.                          \tag{10}
\]

The lower witness above uses h-q letters, between1 and h; the upper
witness uses h+q+1<=2h. Owners themselves use h+1<=2h. Thus every
nonempty proper target has a cyclic D witness of length at most2h.

To control the period, let J(A) be the sum modulo n of the indices of
equal adjacent bit pairs. At the unmatched zero u, local001 becomes100
under f. The equal edge moves from u-1 to u, while all others retain
their equality indicator. Thus J(fA)=J(A)+1 and J(gA)=J(A)+2 modulo n.
Odd n implies every g-period v is divisible by n. Consequently

    v>=n=2r+1>2h.

The collar2h-1 therefore supplies every crossing witness of length at
most2h as an ordinary nonwrapping interval. Concatenating the cycle words
preserves those witnesses. The full ground set occurs as the union of
the entire word because all singletons occur. This proves (6) with
complete target coverage and all joins charged.

## 5. Finite reflection count for the whole overhead

Because v>=n and2h-1>0,

\[
 \sum_{\mathcal C}(2h_{\mathcal C}-1)
 \le\frac1n\sum_{|A|=r}(2h(A)-1).                         \tag{11}
\]

For each labelled binary word with its given linear cut, write its
partial-sum maximum and minimum as M,m. The endpoint is-1 and h(A)<=M-m.
Reflection at the first hit of positive or negative level a gives

\[
 \#\{A:M\ge a\}=\binom n{r-a},\qquad
 \#\{A:-m\ge a\}=\binom n{r+1-a}.
\]

Summing the tails and using odd-binomial symmetry proves exactly

\[
 \sum_{|A|=r}(M-m)
   =\sum_{j=0}^{r-1}\binom nj+\sum_{j=0}^{r}\binom nj
   =2^n-W_r.                                                \tag{12}
\]

Equations (11)-(12) bound the integer overhead in (6) by
floor((2^(n+1)-3W_r)/n), proving (1). The literal trimmed lift proves
(2). The central-binomial estimate then proves (3); more precisely the
upper envelope is1+sqrt(2pi/k)-3/k+O(k^-3/2).

For the explicit thresholds put t_r=2^(2r+1)/W_r and
e_r=(2t_r-3)/(2r+1). The exact ratio
t_(r+1)=t_r(2r+4)/(2r+3) gives

\[
 e_r-e_{r+1}=
 \frac{2t_r(2r+5)-6(2r+3)}{(2r+1)(2r+3)^2}>0.
\]

At r=1 use t_1=8/3; afterwards t_r>=16/5>3. Exact integer checks give
e_283>1/10>e_284 and e_31115>1/100>e_31116. Monotonicity and the exact
even lift establish (4).

[The full period, erosion, reflection and rounding audit](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_HEIGHT_ADAPTIVE_FINITE_WORD_AND_RANGE_BOUND_INDEPENDENT_AUDIT_20260908.md)
contains the complete proof. Root read both main proof notes and the
retained global-maximum corridor proof and checked the finite accounting.
[A further full synthesis audit](/Users/amir.nuriyev/Documents/problem/scratch/HEIGHT_ADAPTIVE_PBBS_ROOT_SYNTHESIS_INDEPENDENT_AUDIT_20260908.md)
also checks the stated witness indices, parity, thresholds and finite
certificate bindings without executing additional mathematics.

## 6. An independently constructed24,957-letter word at17

One fixed deterministic h100 construction found146 cycles with total
height519. Starting each lower cycle at its least integer mask and
ordering cycles by those minima, the full theorem recipe has length

    24310+2*519-146=25202.

It is universal. Trimming each collar to h gives24829 letters with
exactly128 holes:65 at rank10,49 at rank11 and14 at rank12. Appending
every missing mask in ascending order gives

\[
\boxed{24313\le\nu(17)\le24829+128=24957.}                 \tag{13}
\]

The user's submitted140-hole/24969-word count used an unspecified cut
and component order. Those choices can change the surviving and
cross-component witnesses. Our fixed convention gives128 holes; no
alternative cuts or order search were tried. The stronger24957 word
was materialized and checked directly.

- [The24,957-letter word](/Users/amir.nuriyev/Documents/problem/answers/k17_upper24957.word)
- [Standalone independent checker](/Users/amir.nuriyev/Documents/problem/scripts/verify_k17_upper24957.py)
- [Root's executed verification report](/Users/amir.nuriyev/Documents/problem/witnesses/k17_upper24957/literal24957_verification.json)
- [All131,071 ordinary interval witnesses](/Users/amir.nuriyev/Documents/problem/witnesses/k17_upper24957/literal24957_target_witnesses.json)
- [Full deterministic generator, cycle data and finite certificates](/Users/amir.nuriyev/Documents/problem/scratch/K17_HEIGHT_ADAPTIVE_25202_AND_REPAIRED24957_EXACT_CERTIFICATE_20260908.md)

The word is whitespace-separated decimal masks, bit x-1 for coordinate x.
Its byte-body SHA-256 is

    dc7c7af32feb73c91fd14e00c6a046de6d753af4d2fc632f71960dcdbdd820db

Both the construction verifier and a separate root-owned literal replay
certified every nonempty target; all131071 saved intervals were rechecked
by an independent segment-tree range OR. All letters are nonzero, and
all endpoints lie in the ordinary word. Mathematical execution occurred
only on h100, with explicit resource caps.

This improves the just-verified25374 upper bound by417, and the earlier
25745 bound by788. The remaining gap to B(17)=24313 is644. The older
words remain stored for provenance. Exact equality is still unproved.
