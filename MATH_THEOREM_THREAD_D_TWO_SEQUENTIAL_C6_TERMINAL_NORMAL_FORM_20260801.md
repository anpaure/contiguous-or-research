# Two sequential same-side `C6` switches: terminal normal form, phase residues, and the exact remaining compound classes

Date: 2026-08-01  
Status: **exact algebraic reduction; literal reachability and terminal-test theorem; no finite existence or no-go claim**

## 1. Literal setup

Let $M$ be one of the two quotient incidence matchings.  Write $m_x$
for its selected literal incidence at owner $x$, and $f_x$ for the facet
of $m_x$.  Parallel incidences between the same owner and facet are retained
as different literals.

A first state-relative `C6` has owner support $A$, oriented assignment
3-cycle $\sigma$, and literals

\[
                 p_x:x\longrightarrow f_{\sigma(x)}
                 \qquad (x\in A).
\tag{1.1}
\]

After this switch, a second state-relative `C6` has support $B$, oriented
3-cycle $\tau$, and terminal literals

\[
                 q_x:x\longrightarrow f_{\sigma\tau(x)}
                 \qquad (x\in B).
\tag{1.2}
\]

Here products act on the right: the terminal facet permutation is

\[
                              \mu=\sigma\tau .
\tag{1.3}
\]

The terminal literal matching is

\[
 e_x=\begin{cases}
 q_x,&x\in B,\\
 p_x,&x\in A\setminus B,\\
 m_x,&x\notin A\cup B.
 \end{cases}
\tag{1.4}
\]

Thus a literal used by the first switch at $A\cap B$ is overwritten and
does not occur in the terminal state.  It remains part of a reachability
witness, but it must not contribute a second time to a terminal palette
ledger.

### Lemma 1.1 (exact literal reachability)

A proposed terminal pair $(\mu,e)$, together with an ordered factorization
$\mu=\sigma\tau$ into 3-cycles, is realized by two state-relative same-side
`C6` switches if and only if:

1. for each $x\in A\setminus B$, the terminal literal $e_x$ is an
   incidence from $x$ to $f_{\sigma(x)}$;
2. for each $x\in B$, $e_x$ is an incidence from $x$ to
   $f_{\sigma\tau(x)}$;
3. for every $x\in A\cap B$, there exists an intermediate literal $p_x$
   from $x$ to $f_{\sigma(x)}$; and
4. the terminal literals form a perfect owner--facet matching.

The intermediate matching is automatically owner- and facet-perfect.  It
may intersect the fixed opposite matching, lose a palette colour, disconnect,
or have zero voltage: none of those intermediate properties is necessary for
an atomic two-switch terminal move.  Only terminal disjointness and terminal
constraints may be imposed.

#### Proof

Necessity is (1.1)--(1.4).  Conversely choose the intermediate literals in
Condition 3 and use the terminal literals on $A\setminus B$ for the other
first-switch rows.  The map $x\mapsto f_{\sigma(x)}$ is a permutation of
the three old facets, hence gives a perfect first matching.  Equation (1.2)
then makes the second switch state-relative, and (1.4) gives the prescribed
terminal matching.  No condition involving the opposite matching was used
before the terminal state.  $\square$

This lemma is also the precise rule for admitting an intermediate choice
equal to an opposite-base incidence: it is legal as a reachability witness
when it is overwritten, although it is not a legal terminal literal.

## 2. Product classification

Put $s=|A\cap B|$.  For $s=2$, the two shared owners inherit an arrow
from a 3-cycle: $u\to v$ if the cycle maps $u$ to $v$.  Call the
orientations **aligned** when they induce the same arrow on the shared pair.

### Theorem 2.1 (two-3-cycle normal form)

Up to relabelling and inversion, every ordered product
$\mu=\sigma\tau$ has exactly one of the following forms.

| $s$ | representatives | terminal cycle type | fixed points in $A\cup B$ |
|---:|---|---|---:|
| 0 | $((abc),(def))$ | $(3)(3)$ | 0 |
| 1 | $((abc),(ade))$ | $(5)$ | 0 |
| 2, aligned | $((abc),(abd))$ | $(ac)(bd)$ | 0 |
| 2, opposite | $((abc),(adb))$ | $(adc)$ | 1 ($b$) |
| 3, equal | $\tau=\sigma$ | $\sigma^2$, a 3-cycle | 0 |
| 3, inverse | $\tau=\sigma^{-1}$ | identity | 3 |

#### Proof

For $s=0$, the cycles commute and remain disjoint.  For $s=1$, direct
composition gives, for the displayed representatives,

\[
                       (abc)(ade)=(a\ d\ e\ b\ c).
\]

For $s=2$, direct composition gives

\[
 (abc)(abd)=(ac)(bd),\qquad
 (abc)(adb)=(adc),\quad b\text{ fixed}.
\tag{2.1}
\]

The two possible orientations on the common pair are exactly the displayed
aligned and opposite cases.  When the supports agree there are only the equal
and inverse oriented cycles, giving $\sigma^2$ and the identity.  $\square$

The independent six-label audit
`scratch/audit_threadD_two_sequential_c6_normal_form_20260801.py`
checks all `1600` ordered pairs.  Its exact census is

| $s$ | cycle type | ordered pairs |
|---:|---|---:|
| 0 | `(3,3)` | 80 |
| 1 | `(5)` | 720 |
| 2 | `(2,2)` | 360 |
| 2 | `(3)` | 360 |
| 3 | identity | 40 |
| 3 | `(3)` | 40 |

At $s=2$, all `360` aligned pairs give `(2,2)` and all `360` opposite
pairs give `(3)`.

## 3. The parallel-label residue

The permutation $\mu$ does not determine the literal terminal state.  Define

\[
 R=\{x\in A\cup B:\mu(x)=x\text{ and }e_x\ne m_x\}.
\tag{3.1}
\]

For $x\in R$, the terminal incidence $e_x$ is parallel to $m_x$: it
has the same owner and facet but may have a different shift/deletion label.
It is a genuine **phase residue**.  Theorem 2.1 gives

\[
 |R|=0\quad(s=0,1;\ s=2\text{ aligned};\ s=3\text{ equal}),
\tag{3.2}
\]

\[
 |R|\le1\quad(s=2\text{ opposite}),\qquad
 |R|\le3\quad(s=3\text{ inverse}).
\tag{3.3}
\]

The bounds are sharp in a quotient multigraph with suitable parallel
incidences.  They cannot be removed from a proof by replacing literal
incidences with owner--facet pairs.  A residue leaves the owner permutation
unchanged but can change both turn palettes and the physical voltage.

## 4. Which states are already single shells?

Assume the base-state raw shell catalogue retains every literal incidence,
deduplicates only complete terminal matching vectors, and imposes only
terminal opposite-matching disjointness.

### Corollary 4.1 (exact shell absorption)

1. Every $s=1$ terminal state is already a literal single `C10` shell.
   All five owners move, so no hidden phase residue exists.
2. Every $s=3$, equal-orientation terminal state is already a literal
   single `C6` shell.
3. An $s=2$, opposite-orientation state is a single `C6` shell exactly
   when its one possible residue is the base incidence.  Otherwise it is a
   disjoint same-side `phase + C6` terminal state.
4. An $s=3$, inverse-orientation state is the no-op when $R=\varnothing$,
   and otherwise is a phase bank on at most three owner--facet pairs.
5. The $s=2$, aligned-orientation state is the genuinely new overlapping
   multi-cycle type: two disjoint assignment transpositions, equivalently an
   atomic pair of literal rectangles on four owners.
6. The $s=0$ state is the other multi-cycle type globally: two disjoint
   assignment 3-cycles.  Because the owner supports are disjoint, the second
   `C6` is already a base-state raw `C6`; no state-relative regeneration is
   needed.

#### Proof

The cycle types follow from Theorem 2.1.  A terminal literal at every moved
owner binds that owner directly to the old facet prescribed by its cycle in
the permutation $\mu$, so a single 5-cycle or 3-cycle is exactly a raw
`C10` or `C6` row.
The only obstruction is a nonbase literal at a fixed point, precisely (3.1).
For disjoint supports, the first switch changes none of the old facets used
by the second support, proving Item 6.  $\square$

Thus, **among overlapping two-C6 histories**, the only new multi-cycle
permutation is the aligned $s=2$ double rectangle.  If disjoint supports
are included, the `(3,3)` pair must additionally be tested.  Phase residues
are lower-dimensional literal banks, not new permutation types.

An important consequence is that intermediate-invalid overwritten labels do
not reopen the single-shell cases.  Their valid terminal `C6`/`C10` matching
is present in the direct shell catalogue independently of how it was reached.

## 5. Exact topology and voltage tests

Let $\pi$ be the base successor permutation.  For a D-side terminal
assignment permutation $\mu$, and an H-side one, respectively,

\[
                 \pi'_D=\pi\mu,\qquad
                 \pi'_H=\mu^{-1}\pi .
\tag{5.1}
\]

Contract the unchanged arcs of the base $\pi$-cycle and let $s_0$ be the
cyclic successor on the selected owners in their $\pi$-order.  Connectivity
is equivalent to

\[
 s_0\mu\text{ being one cycle on D},\qquad
 \mu^{-1}s_0\text{ being one cycle on H}.
\tag{5.2}
\]

For the double-rectangle type $\mu=(ab)(cd)$, (5.2) is equivalent to the
two chords having alternating endpoints in the base cyclic order: after the
first transposition splits the cycle, the endpoints of the second must lie in
different components.  This is the exact interlacing test.

When the terminal factor is connected, its voltage change is

\[
 \Delta v_D=\sum_x\bigl(\operatorname{sh}(e_x)-
                         \operatorname{sh}(m_x)\bigr),\qquad
 \Delta v_H=\sum_x\bigl(\operatorname{sh}(m_x)-
                         \operatorname{sh}(e_x)\bigr).
\tag{5.3}
\]

with the sum restricted to changed literals and interpreted for the side
being switched.  Phase residues in $R$ occur in this sum.  Therefore
nonzero voltage is a literal terminal test, not a function of $\mu$.

## 6. Palette atomicity

Let $N$ be the unchanged opposite matching.  At every changed owner and
facet, delete the old turn once and insert the turn formed by terminal
$(e,N)$ once.  Equivalently, rebuild all lower and upper turns from the two
terminal matchings.  One must not add the two separate C6 palette columns:
at $A\cap B$ the first literal is overwritten, and at a phase residue the
permutation delta is zero while the literal palette delta need not be.

This gives the following proof-safe completeness checklist for a sequential
enumerator.

1. Retain all first raw 3-cycles, including parallel labels and labels equal
   to the fixed opposite matching.
2. Generate the second raw 3-cycle relative to the literal first matching.
3. Do not enforce opposite disjointness, palette, topology, or voltage at the
   intermediate state.
4. Deduplicate by the complete terminal owner-to-incidence vector, never only
   by $\mu$ or its support.
5. Enforce terminal owner/facet perfectness and terminal opposite disjointness.
6. Recompute terminal palettes atomically, then topology and voltage.
7. If a direct terminal-state catalogue is used instead of histories, retain
   a factorization witness satisfying Lemma 1.1 before accepting a positive.
   A no-go on a literal terminal superset is valid without such witnesses.

## 7. Candidate29 consequence and precise open scope

For candidate29, the complete one-side `C6` and `C10` shells are already
closed.  Hence a sequential same-side search need not revisit:

* $s=1$;
* $s=3$ with equal orientations; or
* $s=2$ with opposite orientations and no phase residue.

The exact remaining terminal classes are:

1. disjoint base-state `C6 + C6` (`s=0`, cycle type `(3,3)`);
2. an interlacing literal double rectangle (`s=2` aligned, type `(2,2)`);
3. same-side `phase + C6` from the one-residue $s=2$ case.

Candidate29 has no H phase and exactly one D phase,
owner/facet `425/295`, incidence `3825 -> 3829`.  This collapses Item 3
to a very small typed bank.  The phase-only terminal states in the inverse
$s=3$ case are already closed: they are either the base no-op or this one
D phase, whose exact replay leaves both candidate29 holes.  The same-side
phase + C6 state does not identify with the already
audited **opposite-side** D-phase x H-C6 class.  No claim about those
same-side residual banks, the two genuine multi-cycle classes, deeper
shadows, residence, or the compiler is made here.
