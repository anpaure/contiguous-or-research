# Independent audit: the first shadow of an exact wreath factor

## Verdict

The principal mathematics in `WREATH_FIRST_SHADOW_RESEARCH.md` is correct:

- the depth-one slot, point-margin, and colour-matching identities are exact;
- the displayed fourteen cyclic orders really are an exact factor of
  \(\binom{[9]}4\) with perfect rank-three coverage;
- Lemma 3.1 is valid;
- the square-resolved four-level bridge is a correct conditional theorem;
- the symbolic lexical collision really prevents the published GJM
  four-level Hamilton cycle from satisfying the first completion injection.

There are two qualifications.

1. Section 1 should explicitly assume \(m\geq2\).  At \(m=1\), cyclic
   intervals of length \(m-1=0\) are all the same empty set, so the assertion
   that a wreath contributes \(n\) distinct depth-one slots and hence
   \(\sum_S\mu(S)=W\) is false with the stated set-valued definition of
   \(\mathcal W_0(C)\).  This is only a harmless small-parameter boundary;
   every asymptotic use has \(m\to\infty\).
2. None of the results in the note proves the weak vertical wreath lemma.
   They solve or reformulate only its \(q=1\) gate.  The four-level bridge is
   one step further removed: it gives a two-coloured path cover, not yet an
   exact odd-dimensional wreath factor, and it gives no depth \(q\geq2\)
   information.

Subject to those qualifications, the note can be retained as a proved
first-shadow research result, not as a new asymptotic OR construction.

## 1. Audit of the exact \(q=1\) identities

Put

\[
 n=2m+1,\qquad W=\binom nm,\qquad
 B=\frac Wn=\operatorname{Cat}_m,\qquad
 N=\binom n{m-1}=\frac{m}{m+2}W.
\]

For \(m\geq2\), the \(n\) cyclic intervals of length \(m-1\) in one
cyclic order are distinct.  Hence \(B\) wreaths contribute exactly
\(nB=W\) slots, proving

\[
 \sum_S\mu(S)=W.
\]

If \(M_1\) colours are absent and
\(E=\sum_S(\mu(S)-1)_+\), then

\[
 W=(N-M_1)+E,
\]

so

\[
 M_1=E-(W-N),\qquad W-N=\frac{2W}{m+2}.
\]

For a fixed coordinate \(x\), exactly \(m-1\) cyclic intervals of length
\(m-1\) in each order contain \(x\).  Summing over the \(B\) orders gives

\[
 \sum_{S\ni x}\mu(S)=(m-1)B.
\]

Finally, the Johnson edges with intersection colour \(S\),
\(|S|=m-1\), live on the \(m+2\) vertices \(S\cup\{a\}\).  At a fixed
middle vertex, the two wreath edges delete the two different boundary
elements of its cyclic block, so they have different intersection colours.
Since the exact factor uses each middle vertex once, all edges of colour
\(S\) form a matching.  Therefore

\[
 0\leq\mu(S)\leq\left\lfloor\frac{m+2}{2}\right\rfloor.
\]

This proves every identity in Section 1.  The only correction is the explicit
\(m\geq2\) hypothesis.

## 2. Independent verification of the fourteen-order certificate

I independently enumerated the ordinary cyclic intervals of lengths four and
three in the fourteen displayed orders.  The check was written in C++ and run
with optimization on the remote compute host, not on the local Mac.  The
verifier is

`scratch/audit_wreath_first_shadow.cpp`

with SHA-256

```text
5d8a72c7c37dad76604cd0ce2ed38628ec7f0afbae8d74594188918c834b691a
```

for the version used for this audit.  Its decisive output is

```text
rank3 targets=84 mult1=42 mult2=42
rank4 targets=126 mult1=126
PASS
```

Thus all \(126\) four-sets occur exactly once, all \(84\) triples occur,
and the triple multiplicity distribution is exactly \(42\) singles and
\(42\) doubles.  This certifies all claims (2.1)--(2.2).

As an additional scope check, this particular perfect-shadow factor has no
rainbow coordinate cut in the stronger sense of Section 3.  The numbers of
distinct internal path intersections for cuts \(1,\ldots,9\) are

\[
 46,47,47,46,46,48,45,52,43
\]

out of the required \(56\).  Therefore Section 2 and the rainbow-cut program
in Section 3 are genuinely different facts: globally perfect first-shadow
coverage does not imply even one rainbow cut.

## 3. Audit of Lemma 3.1

Fix a coordinate \(z\).  Removing the position of \(z\) from a cyclic order
leaves a linear order on \(2m\) points.  The \(m+1\) middle \(m\)-windows
avoiding \(z\) are consecutive and form a Johnson path

\[
 X_0^z,X_1^z,\ldots,X_m^z,
 \qquad X_m^z=\overline{X_0^z}.
\]

Its \(m\) edge intersections are \((m-1)\)-sets avoiding \(z\).  Across
the \(B\) wreaths there are

\[
 mB=\frac{m}{m+1}\binom{2m}{m}
    =\binom{2m}{m-1}
\]

such slots, exactly the number of \((m-1)\)-sets avoiding \(z\).  Hence
pairwise distinctness is equivalent to exact coverage of that sector.

If every \(z\in Z\), \(|Z|=t\), is rainbow and a target \(S\) is missing,
then \(S\) cannot avoid any member of \(Z\).  Thus \(Z\subseteq S\), giving

\[
 M_1\leq\binom{n-t}{m-1-t},
\]

with the usual convention that this is zero if \(t>m-1\).  Dividing by
\(W\) gives exactly

\[
 \frac{\binom{n-t}{m-1-t}}{\binom nm}
 =\frac{(m)_{t+1}}{(m+2)(2m+1)_t}
 =2^{-t}\exp\!\left(O(t^2/m)\right)
\]

for \(t=o(\sqrt m)\).  If more than \(o(\sqrt m)\) rainbow cuts are
available, one may simply retain a divergent \(o(\sqrt m)\)-sized subset.
Thus the stated conclusion \(t\to\infty\Rightarrow M_1=o(W)\) is valid.

What this proves is only the first summand needed in

\[
 \sum_{q=1}^{H}M_q=o(W).
\]

It supplies no relation between a rainbow cut at depth one and defects at
depths \(q\geq2\).

## 4. Audit of the square-resolved four-level bridge

Let

\[
 V=\binom{2m-1}{m-1},\qquad
 L=\binom{2m-1}{m-2},\qquad
 B=V-L=\operatorname{Cat}_m.
\]

A Hamilton cycle in the four stated levels has \(2V+2L\) vertices.  Every
one of the \(2L\) outer vertices consumes two distinct cycle edges, so after
suppressing the outer vertices the resulting Hamilton cycle \(G\) on the
\(2V=\binom{2m}{m}\) mapped middle vertices contains

\[
 2L\quad\text{outer-derived edges},\qquad
 (2V+2L)-4L=2B\quad\text{central edges}.
\]

The three edge types have exactly the colours stated in (4.3)--(4.5):

- a lower suppressed edge has meet \(T\cup\{z\}\) and join
  \(\alpha(T)\cup\{z\}\);
- an upper suppressed edge has meet \(\sigma(U)\) and join \(U\);
- a central edge \(S\subset A\) has meet \(S\) and join
  \(A\cup\{z\}\).

If \(\alpha\) and \(\sigma\) are injective, their two residual colour sets
both have size \(V-L=B\).  A central perfect matching between those residual
sets supplies every residual lower and upper colour once.  Keeping it and all
outer-derived edges deletes exactly the other \(B\) central edges from the
single cycle \(G\).  A cycle with \(B\geq1\) deleted edges is a spanning
union of exactly \(B\) paths, and the retained edge count is

\[
 2L+B=V+L=\binom{2m}{m-1}.
\]

This proves Theorem 4.1 exactly.

The hypotheses beyond existence of the four-level Hamilton cycle remain
unproved.  Even under them, the theorem does not yet produce an exact wreath
factor.  To do that, every path must have exactly \(m\) edges and complementary
endpoints.  The internal meets would then cover the \(z\)-free lower first
shadow, while the joins are needed to complete the \(z\)-containing middle
layer.  The remaining \(z\)-containing lower first-shadow colours depend on
consecutive unions \(Y_{i-1}\cup Y_i\), as recorded in (6.2).  No bridge
hypothesis controls those pairs, and none controls deeper shadows.

## 5. Audit of the GJM lexical obstruction

Set \(r=m-1\).  A lower outer vertex in the GJM construction is a binary
word of length \(2r+1\) with \(r-1\) up-steps and \(r+2\) down-steps.  Its
two lower lexical neighbours flip scan indices \(r\) and \(r+1\), i.e. the
last two down-steps in the row-wise lexical scan.

For Dyck words \(w,v\) with total semilength \(r-2\), consider

\[
 x=w\,00010\,v,\qquad x'=w\,00001\,v.
\]

In \(x\), the final two down-steps in lexical order are gadget positions
five and three.  In \(x'\), they are gadget positions three and four.  The
reason is that all down-steps of the final shifted Dyck word \(v\) on the
same row lie to the right and are scanned earlier, while position four of
the second gadget is the unique down-step on the next lower row.  Flipping
the two selected positions produces the same completion in both cases:

\[
 w\,00111\,v.
\]

The decomposition is recoverable from the maximal initial Dyck prefix, so
different pairs \((w,v)\) give distinct collision pairs and distinct common
completion colours.  Catalan convolution gives

\[
 \sum_{a+b=r-2}\operatorname{Cat}_a\operatorname{Cat}_b
 =\operatorname{Cat}_{r-1}
 =\operatorname{Cat}_{m-2}.
\]

Thus the lower square-completion map is noninjective for every \(m\geq3\).
The GJM paper constructs its Hamilton cycle from the lexical cycle factor by
symmetric differences with 6-cycles entirely in the upper two levels.  Those
switches leave every lower outer two-path unchanged, so all the displayed
collisions survive in the final Hamilton cycle.  The claimed obstruction is
therefore valid.

This is an obstruction to that particular lexical Hamilton cycle, not to
Theorem 4.1 in general.  Moreover, \(\operatorname{Cat}_{m-2}=O(B)\) is
small compared with the full middle width, so the theorem still permits a
Catalan-scale rewiring of the lexical construction; it merely proves that no
zero-rewiring use of it can work.

## 6. Exact contribution to the general program

The audited results occupy the following positions in the proof hierarchy.

| Result | Proved contribution | What is still absent |
|---|---|---|
| Slot and margin identities | Exact collision ledger at \(q=1\) | No construction and no \(q\geq2\) control |
| Fourteen-order \(m=4\) certificate | Zero first-shadow defect is feasible in one nontrivial dimension | No all-\(m\) family; it has zero rainbow cuts |
| Many-rainbow-cuts lemma | A sufficient condition for \(M_1=o(W)\) | No factor with \(t\to\infty\) is constructed; no deeper depths |
| Square-resolved bridge | Conditional exact two-sided first-shadow path cover | Its extra hypotheses are open; paths are not wreaths; no deeper depths |
| GJM collision theorem | Eliminates the unchanged published lexical Hamilton cycle as an instance of the bridge | Does not obstruct nonlexical cycles or Catalan-scale rewiring |

Consequently, this pass makes genuine structural progress on the first
shadow, but it does **not** advance the proved asymptotic bound.  The weak
wreath-factor lemma still requires one exact factor satisfying the aggregate
multiscale estimate

\[
 \sum_{q=1}^{H}M_q=o(W),
\]

and no result here controls any summand with \(q\geq2\).  The cleanest honest
next target is a multidepth analogue of the rainbow-cut lemma, or a mechanism
that converts a square-resolved complementary path factor into wreaths while
simultaneously controlling consecutive higher-order meet/union colours.
