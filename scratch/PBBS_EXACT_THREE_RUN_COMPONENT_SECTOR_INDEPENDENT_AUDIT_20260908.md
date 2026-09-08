# Independent audit of the exact PBBS three-run component sector

Date: 2026-09-08. Reviewer: Codex subagent exact_equality_structure.

Reviewed source:

    scratch/PBBS_EXACT_THREE_RUN_COMPONENT_SECTOR_20260908.md

Verdict: the all-r theorem is valid from the explicitly imported PBBS root
map and gap-five classification. No gap was found in the new component
classification. This is a mathematical audit, not a rerun of the author's
h100 finite verifier.

The dependency note
MATH_THEOREM_PBBS_EXACT_RUN_SPECTRUM_FLAT_ANTECEDENT_NOGO_AND_FULL_UPPER_DECK_20260813.md
does supply the required gap/run dictionary, absence of gaps one and three,
and exact gap-five starting roots. Its positive run of length three is
associated with a gap-five root, not an arbitrary height-two state.

For r>=3, a Dyck word with r-1 peaks has precisely one double ascent and
one double descent. Nonnegativity puts them in that order, giving the
unique triple form

    D(x,y,z)=(10)^x 1(10)^(y+1) 0(10)^z,
    x+y+z=r-2.

At its first height-two up-step,

    P=(10)^x 1,
    Q=0(10)^y 0(10)^z.

Direct concatenation in phi(D)=complement(Q) 0 complement(P) gives
D(y,z,x). The new physical root is displaced by |P|+1=2(x+1).
After three applications the root therefore advances by
2(x+y+z+3)=2r+2, or one modulo n=2r+1.

Every nonconstant triple orbit has length three. Its physical f-orbit has
length exactly 3n: returning to the triple requires a multiple of three
steps and the corresponding root increments have exact order n. Since
3n is odd, taking successor f^2 does not split that component. A fixed
triple, when it exists, has all coordinates positive for r>=3 and hence
cannot belong to the boundary sector.

The imported gap-five form is precisely z=0. Rotation of the triple
therefore meets a gap-five root exactly when at least one coordinate is
zero. For N=r-2>=1 there are 3N boundary triples: 3(N-1) with one zero
and three with two zeros. All have triple-orbit size three. Hence there
are exactly N=r-2 bad owner components, each with 3n states. Invariance
of the triple class and the converse gap-five classification exclude a
short positive run hidden in any other component.

At r=8 this gives six 51-cycles, totaling 306 owners. One triple orbit
has two zero phases and the other five have one, so the total short-run
count is 17(2+5)=119. These agree with the imported global gap-five count.

The final construction qualification is necessary and correctly stated:
this classifies intact canonical components. It does not prove a safe
fusion, preservation of upper witnesses through component cuts, or a
306-owner prefix whose newly created seams preserve the advertised
residence. The variable-depth compiler still needs those properties.
