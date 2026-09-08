# Independent audit of growing transversal-face packing

## 1. Verdict

The main theorem in `GROWING_TRANSVERSAL_FACE_PACKING.md` is valid.
For every fixed `0<alpha<1`, with

\[
 s=\lfloor\alpha\log_2\log m\rfloor,
 \qquad k=2^s,
\]

the matching-face hypergraph has a matching whose uncovered middle-vertex
fraction is

\[
                  O\!\left(
                  e^{-c_\alpha(\log m)^{1-\alpha}}
                  \right)                            \tag{1.1}
\]

for some `c_alpha>0` and all sufficiently large `m`.

The following minor repairs were made to the source note.

1. Corollary 1.5 of the primary paper assumes `k>4`; this is eventually
   true here and is now stated.
2. The paper uses natural logarithms; the source now fixes that convention.
3. The coverage statement is written with an explicit upper-error `O(...)`
   rather than the less precise `1-exp{-Omega(...)}` notation.
4. The polynomial-depth comparison is identified as a limitation of the
   **guaranteed bound**, not a lower bound on the optimal matching.
5. “Diversification” was weakened to “face packing”, because the matching
   theorem does not control the distribution of active pair systems.

No mathematical hypothesis or exponent failed.

## 2. Primary-source theorem

The audit used the complete primary paper:

Noga Alon, Bela Bollobas, Jeong Han Kim, and Van H. Vu,
[*Economical covers with geometric applications*](https://web.math.princeton.edu/~nalon/PDFS/abkv4.pdf),
especially Corollary 1.5.

The paper explicitly permits `k` and the number of vertices to vary with
`D`, takes all unmarked logarithms to base `e`, and states the following
matching result for `k>4`:

> A `D`-regular `k`-uniform hypergraph with maximum codegree `C` has a
> matching leaving
>
> \[
> O\!\left(
> k\left({C\log(1+C)\over D}\right)^{1/(k-1)}n
> \right)                                             \tag{2.1}
> \]
>
> vertices uncovered, provided
>
> \[
>                         e^{2k}C=o(D/\log D).         \tag{2.2}
> \]

Thus the source note correctly invokes a matching corollary, not merely the
paper's cover theorem.  The `k` factor, the exponent `1/(k-1)`, the
`log(1+C)` term, and the side condition (2.2) are all transcribed exactly.

## 3. Hypergraph substitution

For the simple hypergraph `F_(m,s)` of distinct `s`-faces, the previously
audited exact parameters are

\[
 n=\binom{2m}m,qquad
 k=2^s,qquad
 D=\binom ms^2s!,qquad
 {C\over D}={s\over m^2}.                            \tag{3.1}
\]

There is no hidden face multiplicity in `D` or `C`: the invisible pairing
between the fixed selected and excluded coordinates was removed when the
simple face hypergraph was defined.

Put

\[
                         L=\log m.
\]

For fixed `alpha in (0,1)`, the floor in the definition of `s` gives

\[
 {1\over2}L^\alpha<k\le L^\alpha                  \tag{3.2}
\]

for all sufficiently large `m`.  In particular, `k->infinity`, `k>4`
eventually, and `k=o(L)`.

Since `s=Theta(log L)=o(m)`, Stirling gives

\[
\begin{aligned}
 \log D
 &=2\log\binom ms+\log(s!)\\
 &=2sL-s\log s+O(s)
 =\Theta(sL).                                       \tag{3.3}
\end{aligned}

All substitutions in the source note agree with (3.1)--(3.3).

## 4. Side-condition audit

The ratio of the left side of (2.2) to `D/log D` is

\[
 R_m=e^{2k}{C\over D}\log D
     =e^{2k}{s\over m^2}\log D.                     \tag{4.1}
\]

Using `k<=L^alpha` and (3.3),

\[
\begin{aligned}
 \log R_m
 &=2k-2L+\log s+\log\log D\\
 &\le2L^\alpha-2L+O(\log L)
 =-2L+o(L)\longrightarrow-\infty.                  \tag{4.2}
\end{aligned}

Therefore `R_m->0`, exactly the little-oh condition (2.2).  The proof has
an exponential margin; it is not relying on an equality case or an
unspecified constant in the theorem.

## 5. Uncovered-fraction exponent

Let

\[
 B_m={C\log(1+C)\over D}.
\]

Since `C<=D`,

\[
 B_m\le {s\over m^2}\log(1+D).
\]

Equations (3.3) and `s=Theta(log L)` imply

\[
                         \log B_m
 \le-2L+O(\log L).                                  \tag{5.1}
\]

For large `m`, `B_m<1`.  Because `k-1<=L^alpha`, multiplying the negative
quantity (5.1) by `1/(k-1)` gives

\[
\begin{aligned}
 \log\left(kB_m^{1/(k-1)}\right)
 &\le \alpha\log L
       -{2L-O(\log L)\over L^\alpha}\\
 &=-2L^{1-\alpha}+o(L^{1-\alpha})\\
 &=-\Omega(L^{1-\alpha}).                          \tag{5.2}
\end{aligned}

Substitution into (2.1) proves (1.1).  The implicit absolute constant in
the `O` term of (2.1) can be absorbed by decreasing `c_alpha`.

The direction of the inequality in (5.2) is correct: since `B_m<1`, the
upper bound `k<=L^alpha` makes `1/(k-1)` at least `L^(-alpha)`, which makes
the power no larger.

## 6. Range and limitations

The proved range `s=alpha log_2 log m`, `alpha<1`, is valid but not asserted
to be optimal.  The primary theorem's side condition alone permits somewhat
larger `k`; obtaining an `o(1)` uncovered fraction additionally requires
the negative term `2L/k` to dominate `log k`.  Nothing in the source note
claims the endpoint.

For any fixed polynomial `H=m^beta`, the guaranteed relative error in
(1.1) is

\[
 e^{-Theta(L^{1-\alpha})},
\]

which is much larger than `1/H=e^{-beta L}`.  Hence this theorem does not
guarantee an absolute leftover `o(W/H)`.  This comparison is only about the
available upper bound; a better object-specific matching is not excluded.

Finally, the ABKV matching covers middle vertices only.  It does not:

* assign standard binary-RSK radii to selected faces;
* supply the exact number of blocks required at each shadow depth;
* control lower- or upper-shadow collisions;
* construct a shifted ordering;
* force a prescribed distribution of active coordinate pairings.

Thus the accepted result is an explicit growing-dimensional middle-face
packing, not an asymptotic universal-OR construction.
